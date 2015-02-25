#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
from baseHandler import BaseHandler
import util.myTools as myTools

class MainHandler(BaseHandler):
    def get(self):
        self.write('Hello TourList!')

    @tornado.web.authenticated
    def post(self):
        self.write('Login Succeed!')
