#!/usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
body{
background-image:linear-gradient(to bottom right,black,white);
background-size:auto;
background-repeat:no-repeat
}
pre{
color:cyan;
font-size:20px;
}
</style>''')

import cgi
import subprocess as sp

field = cgi.FieldStorage()
cmd = field.getvalue("cmd")
cmd = cmd.lower()

if (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('date' in cmd) or ('time' in cmd) or('month' in cmd) or ('year' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo date')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('calendar' in cmd) or ('cal' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo cal -hy')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('docker' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo systemctl start docker')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('stop' in cmd) or ('shut' in cmd) or ('shutdown' in cmd) or ('deactivate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('kill' in cmd) or ('end' in cmd) or ('terminate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('firewall' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo systemctl stop firewalld')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('list' in cmd) or ('folder' in cmd) or ('directory' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo ls')
        print("<pre>",result,"<pre>")
        
elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('ip' in cmd) or ('address' in cmd) or ('mac' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo ifconfig')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('tell' in cmd) or ('active' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('process' in cmd) or ('processes' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo ps -aux')
        print("<pre>",result,"<pre>")

elif (('what' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('name' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('user' in cmd) or ('username' in cmd) or ('account' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo whoami')
        print("<pre>",result,"<pre>")

elif (('what' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('tell' in cmd) or ('access' in cmd) or ('get' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('name' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('terminal' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo tty')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('usage' in cmd)) \
        and (('ram' in cmd) or ('memory' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo free -m')
        print("<pre>",result,"<pre>")

elif (('what' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('tell' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('current' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('directory' in cmd) or ('folder' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('pwd')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('tell' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('what' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('history' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo history')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('docker' in cmd)) and (('status' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo systemctl status docker')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('running' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('docker' in cmd) or ('show' in cmd) or ('initialised' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('os' in cmd) or ('operating system' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo docker ps')
        print("<pre>",result,"<pre>")

elif (('open' in cmd) or ('execute' in cmd) or ('run' in cmd) or ('start' in cmd) or ('access' in cmd) or ('get' in cmd) or ('activate' in cmd) or ('begin' in cmd) or ('get' in cmd) or \
        ('go' in cmd) or ('show' in cmd) or ('initiate' in cmd) or ('launch' in cmd) or ('proceed' in cmd) or ('enter' in cmd)) \
        and (('os' in cmd) or ('operating system' in cmd)) and (('installed' in cmd) or ('all' in cmd) or ('available' in cmd)) and (not(('dont' in cmd) or ("don't" in cmd) or ('do not' in cmd) or ('prevent' in cmd) or ('restrict' in cmd) or ('avoid' in cmd))):
        result = sp.getoutput('sudo docker ps -a')
        print("<pre>",result,"<pre>")
else:
    print('<font>currently the operation is not supported.</font>')
    


