<h2>A very basic Ansible dynamic inventory script for Consul</h2>

<h3>How did we get here? </h3>
<p style="text-align:justify;">I decided to start learning Ansible some time ago. The moment I noticed the dynamic inventory chapter in the <a href="https://docs.ansible.com/ansible/latest/">documentation</a>, my interest was peaked. Since I have played around with <a href="https://www.consul.io">Consul</a> in the past, I knew I had to take a look at the <a href="https://github.com/ansible/ansible/tree/stable-2.9/contrib/inventory">scripts</a> provided by the Ansible community.</p>
<p style="text-align:justify;">So I read the instructions, downloaded the consul_io script and .ini file, started up my lab, wrote a playbook and executed the command. Nothing happened, except Python complaining about errors I knew very little about. Next step was to take a better look at the consul_io.py script, and see what makes it tick. I got the gist of it but found it overly complex for what I needed it for, a small home lab, so I made my own script!</p>

<h3>Lab Setup</h3>
<p>The whole lab is virtual and is being run in <a href="https://www.virtualbox.org">Virtualbox</a>, on a Windows laptop. I'm using a Linux Lite VM as my Consul server and four Alpine Linux VM's as nodes.</p>
