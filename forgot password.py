#!/usr/bin/python3

print("content-type:text/html")
print()

print('''<style>
body{
background-image:linear-gradient(to bottom right,black,white);
background-size:auto;
background-repeat:no-repeat
}
a{
text-decoration:none;
color:palegreen;
}
</style>''')

import cgi
import credentials as cr
field=cgi.FieldStorage()
user=field.getvalue("username")
pwd=field.getvalue("pwd")
confirm_pwd=field.getvalue("confirmpwd")

if pwd==confirm_pwd:
	result=cr.forgot_password(user,pwd)
	if result:
		print('<br/><br/><h3 align="center" style="color:cyan"> Password changed successfully !   </h3>')

	else:
		print('<br/><br/><h3 align="center" style="color:cyan"> User not found. </h3>')
else:
	print('<br/><br/><h3 align="center" style="color:cyan"> Password does not match.Please check ! </h3>')
print('<br/> <center> <a href="/login.html" > Go to Login </a> </center>')
