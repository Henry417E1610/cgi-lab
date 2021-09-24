#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os

from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie



print(login_page())
