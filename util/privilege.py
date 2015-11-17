#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import *
import util.myTools as myTools
from bson.objectid import ObjectId

RELATION_FRIEND = 1
RELATION_STRANGER = 0
PRIVILEGE_CONTENT = 8
PRIVILEGE_SHOWN = 4
PRIVILEGE_ATTEND = 2
PRIVILEGE_SHARE = 1


def has_privilege(privilege, PRIVILEGE_CODE):
    if privilege & PRIVILEGE_CODE == PRIVILEGE_CODE:
        return True
    else:
        return False


def cal_privilege(privilege_list):
    '''
    privilege_list = [
        friend_content, friend_space, friend_attend, friend_share,
        stranger......,
    ]
    '''
    res = 0
    for i in privilege_list:
        res <<= 1
        res += i
    return res


def get_privilege(privilege, relation):
    if relation == RELATION_FRIEND:
        return privilege >> 4
    elif relation == RELATION_STRANGER:
        return privilege & 15
    else:
        return 0


def get_lists_of_user_to_guest(user, guest, rel):
    relation = get_relation(user, guest, rel)
    if relation == RELATION_FRIEND:
        pri = 64
    elif relation == RELATION_STRANGER:
        pri = 4
    else:
        pri = 255

    tlists = CalCollection.find_one({"author": user["name"]})
    for tlist in tlists:
        if tlist['privilege']&pri != pri:
            tlists.remove(tlist)

    return tlists
