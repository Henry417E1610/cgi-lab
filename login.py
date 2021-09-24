#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os

from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie

print("Content-Type: text/html")

#print(login_page())

msg=cgi.FieldStorage()
username=msg.getvalue("username")
password=msg.getvalue("password")
print("<p>%s %s;</p>" % (username, password))

ck=SimpleCookie(os.environ["HTTP_COOKIE"])
user=None
pw=None

if ck.get("username"):
    user=ck.get("username").value

if ck.get("password"):
    pw=ck.get("password").value

if user==secret.username and pw==secret.password:
    username=user
    password=pw


print("<p>%s %s;</p>" % (username==secret.username, secret.password==password))

if username==secret.username and password==secret.password:
    print("Set-Cookie: Username=%s"%username)
    print("Set-Cookie: Password=%s"%password)


if username==None or password==None:
    print(login_page())
elif username==secret.username and password==secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello World</title>')
print('</head>')
print('<body>')
print("<p><b>Username: </b> %s <br><b>Password: </b> %s</p>" %(username,password))
print('</body>')
print('</html>')

