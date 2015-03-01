#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import getpass

def testLogin():
    # email = raw_input('input email: ')
    # password = getpass.getpass('input password: ')
    email = 'rightpeter@163.com'
    password = '123456'
    data = {'email': email, 'password': password}
    post_data = urllib.urlencode(data)
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    headers = {'User-agent': 'Mozillar/4.0 compatible; MSIE 6.0; Windows NT 5.1'}
    url = 'http://localhost:2358/api/login'
    req = urllib2.Request(url, post_data, headers)
    print '------login------'
    try:
        content = opener.open(req)
        print content.read()
    except Exception, e:
        print e

    cj.save('login_cookie.txt')
    url = 'http://localhost:2358/'
    req = urllib2.Request(url, '', headers)
    print '------localhost/------'
    try:
        content = opener.open(req)
        print content.read()
    except Exception, e:
        print e

def testIndex():
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    headers = {'User-agent': 'Mozillar/4.0 compatible; MSIE 6.0; Windows NT 5.1'}
    url = 'http://localhost:2358/'
    req = urllib2.Request(url, '', headers)
    print '-------localhost/ without login cookie-------'
    try:
        content = opener.open(req)
        print content.read()
    except Exception, e:
        print e

    cj.load('login_cookie.txt')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    print '-------localhost/ with login cookie-------'
    try:
        content = opener.open(req)
        print content.read()
    except Exception, e:
        print e

if __name__ == '__main__':
    testLogin()
    testIndex()
