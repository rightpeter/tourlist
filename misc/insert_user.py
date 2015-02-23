#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import util.myTools as myTools

def insert_rightpeter():
    user = {}
    user['email'] = '327888145@qq.com'
    user['name'] = 'Rightpeter'
    user['password'] = '123qweasdzxc'
    if myTools.insert_a_user(user):
        print 'Insert Rightpeter Successfully!'
    else:
        print 'Insert Rightpeter Failed!'

if __name__=="__main__":
    insert_rightpeter()
