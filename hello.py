#!/usr/bin/env python3
import os,json
from templates import login_page, secret_page, after_login_incorrect
import secret

import cgi
import cgitb
cgitb.enable()

from http.cookies import SimpleCookie

print("Type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

print(os.environ)
obj=json.dumps(dict(os.environ), indent=4)
print(obj)

for para in os.environ.keys():
    if para=="QUERY_STRING":
        print("<b>%20s</b>: %s<br>" % (para, os.environ[para]))

print('\r\n\r\n')
for para in os.environ.keys():
    if para=="HTTP_USER_AGENT":
        print("<b>%20s</b>: %s<br>" % (para, os.environ[para]))

print('\r\n\r\n')
for para in os.environ.keys():
    if para=="HTTP_COOKIE":
        print("<b>%20s</b>: %s<br>" % (para, os.environ[para]))
