#! /usr/bin/python3

print("content-type:text/html")
print()

print('''<style>
body{
background-image:linear-gradient(to bottom right,black,white);
background-size:auto;
background-repeat:no-repeat;
}
.center{
position:absolute;
top:50%;
left:50%;
-ms-transform:translate(-50%,-50%);
transform:translate(-50%,-50%);
}
#head{
color:yellow;
font-size:25px;
font-weight:bold;
}
input[type=submit]
{
background-color:crimson;
color:white;
border:none;
border-radius:5px 10px;
font-size:16px;
cursor:pointer;
padding:6px 12px;
}
input[type=text]
{
padding:4px 18px;
border:2px solid lavender;
font-size:15px;
border-radius:5px;
width:400px;
}
</style>''')

import cgi
import credentials as cr
field = cgi.FieldStorage()
user = field.getvalue("username")
pwd = field.getvalue("pwd")

result=cr.authenticate(user,pwd)
if result:
	print('''<form class="center" action="http://127.0.0.1/cgi-bin/main.py">
			<center id="head"> Chat with Your Need </center>
			<br/>
		 	<center> <input placeholder="chat" type="text" name="cmd" /> </center>
			<br/>
			<center> <input type="submit" value="Proceed" /> </center>
		</form>''')
elif result==2:
	print('<br/><br/><h3 align="center" style="color:cyan"> Invalid Password !</h3>')
else:
	print('<br/><br/><h3 align="center" style="color:cyan"> User not found !</h3>')
		
