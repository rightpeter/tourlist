#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from baseHandler import BaseHandler
from operation import admincore
import traceback
from model import *


class APISignupHandler(BaseHandler):
    def check_xsrf_cookie(self):
        pass

    def post(self):
        try:
            user = {}
            user['email'] = self.get_argument('email')
            user['name'] = self.get_argument('name')
            user['password'] = self.get_argument('password')
            raw_password = user['password']
            re_password = self.get_argument('re_password')

            if admincore.is_email_exist(user['email']) or admincore.is_name_exist(user['name']):
                raise Exception('Duplicate email or name!')

            if user['password'] != re_password:
                raise Exception('Password error!')

            if admincore.insert_a_user(user):
                user = admincore.login(user['email'], raw_password)
                if user:
                    self.set_secure_cookie('name', user['name'])
                    self.write('Signup Succeed!')
        except:
            print traceback.print_exc()
            self.write('Signup Failed!')


class APILoginHandler(BaseHandler):
    def check_xsrf_cookie(self):
        pass

    def post(self):
        try:
            email = self.get_argument('email')
            password = self.get_argument('password')

            user = admincore.login(email, password)
            if user:
                self.set_secure_cookie('name', user['name'])
                self.write('Login Succeed!')
        except:
            print traceback.print_exc()
            self.write('Login Failed!')


class APILogoutHandler(BaseHandler):
    def check_xsrf_cookie(self):
        pass

    @tornado.web.authenticated
    def post(self):
        self.clear_cookie('name')
        self.write('Logout Succeed!')
