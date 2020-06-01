# ansible-consul-dynamic-inventory-script
A very basic Ansible dynamic inventory script for Consul

How did we get here? :
I decided to start learning Ansible some time ago. The moment I noticed the dynamic inventory chapter in the documentation, my interest was peaked. Since I have played around with Consul in the past, I knew I had to take a look at the scripts provided by the Ansible community (https://github.com/ansible/ansible/tree/stable-2.9/contrib/inventory).
So I read the instructions, downloaded the consul_io script and .ini file, started up my lab, wrote a playbook and executed the command. Nothing happened, except Python complaining about errors I knew very little about. Next step was to take a better look at the consul_io.py script, and see what makes it tick. I got the gist of it but found it overly complex for what I needed it for, a small home lab, so I made my own script!

Lab Setup:
The whole lab is virtual and is being run in Virtualbox, on a Windows laptop. I'm using a Linux Lite VM as my Consul server and four Alpine Linux VM's as nodes.

What's next? :
I plan to add more functionality to this script, and hopefully submit it to the Ansible community GitHub page.
