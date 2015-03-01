#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import getpass

def testSignup():
    # email = raw_input('input email: ')
    # name = raw_input('input name: ')
    # password = getpass.getpass('input password: ')
    # re_password = getpass.getpass('input password again: ')
    email = 'rightpeter@163.com'
    name = 'rightpeter'
    password = '123456'
    re_password = '123456'
    data = {'email': email, 'name': name, 'password': password, 're_password': re_password}
    post_data = urllib.urlencode(data)
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    headers = {'User-agent': 'Mozillar/4.0 compatible; MSIE 6.0; Windows NT 5.1'}
    url = 'http://localhost:2358/api/signup'
    req = urllib2.Request(url, post_data, headers)
    content = opener.open(req)
    print content.read()
    cj.save('signup_cookie.txt')

if __name__ == '__main__':
    testSignup()
