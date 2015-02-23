#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import util.myTools as myTools
import util.calendar_tools as calendar_tools

def test_add_240_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '240'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 240
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_224_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '224'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 224
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_192_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '192'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 192
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_64_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '64'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 64
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_255_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '255'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 255
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_254_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '254'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 254
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_252_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '252'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 252
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

def test_add_244_event_to_rightpeter():
    user = myTools.get_user_by_name('Rightpeter')
    birthday_event = {}
    birthday_event['title'] = '244'
    birthday_event['starttime'] = '2015-06-22 00:00:00'
    birthday_event['endtime'] = '2015-06-22 23:59:59'
    birthday_event['allday'] = 1
    birthday_event['privilege'] = 244
    res = calendar_tools.add_event_to_user(birthday_event, user)
    print 'res: ', res

if __name__ == '__main__':
    test_add_240_event_to_rightpeter()
    test_add_224_event_to_rightpeter()
    test_add_192_event_to_rightpeter()
    test_add_64_event_to_rightpeter()
    test_add_255_event_to_rightpeter()
    test_add_254_event_to_rightpeter()
    test_add_252_event_to_rightpeter()
    test_add_244_event_to_rightpeter()
