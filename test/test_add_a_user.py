#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import util.myTools as myTools
import util.calendar_tools as calendar_tools

def test_add_a_user():
    user = {}
    user['email'] = 'rightpeter@163.com'
    user['name'] = 'june_fiend'
    user['password'] = 'hehehehehe'
    res = myTools.insert_a_user(user)
    print 'res: ', res

if __name__ == '__main__':
    test_add_a_user()
