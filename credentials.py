#!usr/bin/python3

import sqlite3
connection=sqlite3.connect("/root/Downloads/database/credentials.db")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cred(username TEXT NOT NULL,password TEXT NOT NULL);")

def register(username,pwd):
	cursor.execute("SELECT * FROM cred WHERE username='{}'".format(username))
	user=cursor.fetchall()
	if user == []:
		cursor.execute("INSERT INTO cred(username,password) VALUES('{}','{}');".format(username,pwd))
		connection.commit()
		connection.close()
		return 1
	else:
		connection.close()
		return 0

def forgot_password(username,pwd):
	cursor.execute("SELECT * FROM cred WHERE username='{}'".format(username))
	user=cursor.fetchall()
	if user == []:
		connection.close()
		return 0
	else:
		cursor.execute("UPDATE cred SET password='{}' WHERE username='{}'".format(pwd,username))
		connection.commit()
		connection.close()
		return 1

def authenticate(username,pwd):
	cursor.execute("SELECT * FROM cred WHERE username='{}'".format(username))
	user=cursor.fetchall()
	if user == []:
		connection.close()
		return 0
	elif user[0][1] == pwd:
		connection.close()
		return 1
	else:
		connection.close()
		return 2
