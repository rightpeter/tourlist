#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
import os

from pymongo import MongoClient

from controller.web import *
from controller.apiHandler import *
from tornado.options import define, options

define("port", default=2358, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', MainHandler),
            ('/api/login', APILoginHandler),
            ('/api/signup', APISignupHandler),
            ('/api/logout', APILogoutHandler)
        ]
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            # 'ui_modules': uimodules,
            'cookie_secret': '#De1rFq@oyW^!kc3MI@74LY*^TPG6J8fkiG@xidDBF',
            'login_url': '/login',
            'xsrf_cookies': True,
            'debug': True
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


def init():
    pass


if __name__ == '__main__':
    init()
    main()
