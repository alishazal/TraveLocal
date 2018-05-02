#!/usr/bin/python3.2
print("Content-Type: text/html \n")

#Initializing html as function for ease
def htmlhead():
	print("<!DOCTYPE HTML><html><head><title>My output</title><link rel='stylesheet' type='text/css' href='../style.css'></head><body>")


htmlhead()

#Importing cgi for the form
import cgi

data=cgi.FieldStorage()

#Variables for the form
name = data['name'].value
email = data['email'].value
time = data['time'].value
area = data['area'].value

#Printing out message for the user
print("<h1> Dear", name + ",<br/><br/> Your request has been noted. <br/> We'll email you 15 minutes before", time,"on", email +  ".<br/>We hope you have a safe ride to", area, "</h1>")

#Closing the html
print("</body></html>")
