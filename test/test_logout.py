#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import getpass

def testLogout():
    cj = cookielib.LWPCookieJar()
    cj.load('login_cookie.txt')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    headers = {'User-agent': 'Mozillar/4.0 compatible; MSIE 6.0; Windows NT 5.1'}
    url_index = 'http://localhost:2358/'
    req_index = urllib2.Request(url_index, '', headers)
    print '-------localhost/ with login cookie-------'
    try:
        print 'cookie: ', cj
        content = opener.open(req_index)
        print content.read()
    except Exception, e:
        print e

    url_logout = 'http://localhost:2358/api/logout'
    req_logout = urllib2.Request(url_logout, '', headers)
    print '-------logout-------'
    try:
        content = opener.open(req_logout)
        print content.read()
        print 'cookie: ', cj
    except Exception, e:
        print e

    req_index = urllib2.Request(url_index, '', headers)
    print '-------localhost/ with logout cookie-------'
    try:
        print 'cookie: ', cj
        content = opener.open(req_index)
        print content.read()
    except Exception, e:
        print e

    cj.save('logout_cookie.txt')

if __name__ == '__main__':
    testLogout()
