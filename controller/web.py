#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
import util.myTools as myTools

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello TourList!')
