#!/usr/bin/env python

import consul
import json
import requests

#The main function. Simply prints the JSON snippet for Ansible, by calling ip_list()
def main():
  #I used json.dumps() method so Ansible can process the outcome
	print json.dumps(ip_list())

#The ip_list() function is where the heavy lifting is happening
def ip_list():
  #Declaring the array where the IP's are going to be stored
  iplist=[]

  try:
    #Asking Consul about the nodes through the Consul API. More info here: https://www.consul.io/api-docs/catalog
    response = requests.get('http://localhost:8500/v1/catalog/nodes')
    
    #if response and response.status_code==200:  <-- TODO: Improve. Shows errors for now

    #Passing the API's JSON response into a variable.
    parsed_data = response.json()

  #Server may not respond...
  except:
    return 'Server Error - Bad Respose'

  #The collected_data variable contains all kinds of info about our nodes in a JSON format. Such info can be their IP, node name,
  #  the name of the datacenter they're a part of, and a few more 

  #Looking through the collected_data variable for the info we're interested in
  for i in parsed_data:
    ip = i.get('Address')  #Getting the IP address for each and everyone of our nodes
    nm = i.get('Node')     #Also, I'm going to need the node names
    
    #The collected_data variable contains info for all of our nodes, even our Consul server (aka leader). I intend to run
    #  Ansible playbooks from the leader computer, and I want the leader's IP to be excluded from the dynamic inventory.
    #  I achieve that by reading all the node names in my cluster and excluding the leader from the inventory list by it's name
      
    #"ConsulLeader" in what I named my leader computer while setting up Consul. If the node has a name other than that...
    if nm!='ConsulLeader':
       #...add it's IP in the array
       iplist.append(ip)

  #Let's count how many different IP's are collected...
  l=len(iplist)
   
  #...because there may be none
  if l == 0:
    return 'No nodes found. Cluster is empty'
    
  #If one or more IP's are discovered, return a JSON response containing the ip_list array.
  #More useful info about what a script should return to Ansible
  # can be found here: https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-inventory-scripts
  else:   
      return {
         'group': {
            'hosts': iplist
          }
       }
#Aaand done! Script starting up by calling main()
main()		

