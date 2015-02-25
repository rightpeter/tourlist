# !/usr/bin/env python
# -*- coding: utf-8 -*-

from baseHandler import BaseHandler

import sys
import os
import re
import time
import json
import tornado
import math
import httplib
import json
import pickle
import datetime
import threading
from config import *
from model import *
import util. myTools as myTools


class APILoginHandler(BaseHandler):
    def post(self):
        try:
            email = self.get_argument('email')
            password = self.get_argument('password')

            if myTools.login(email, password):
                user = UserCollection.find_one({'email': email})
                self.set_cookie('login', 'True')
                self.set_secure_cookie('name', user['name'])
                self.write('Login Succeed!')
        except:
            self.set_cookie('login', 'False')
            self.write('Login Failed!')

class APISignupHandler(BaseHandler):
    def post(self):
        try:
            user = {}
            user['email'] = self.get_argument('email')
            user['name'] = self.get_argument('name')
            user['password'] = self.get_argument('password')
            re_password = self.get_argument('repassword')

            if myTools.is_email_exist(user['email']) or myTools.is_name_exist(user['name']):
                raise Exception('Duplicate email or name!')

            if user['password'] != re_password:
                raise Exception('Password error!')

            if myTools.insert_a_user(user):
                if myTools.login(user['email'], user['password']):
                    self.set_secure_cookie('guest', user['name'])
                    self.write('Signup Succeed!')
        except e:
            self.write('Signup Failed!')
