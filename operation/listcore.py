#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import *
from bson.objectid import ObjectId
from util import privilege


def get_list_detail(lid, guest_name):
    try:
        tlist = ListCollection.find_one({'_id': ObjectId(eid)})
    except Exception, e:
        print 'get_list_by_id: ', e
        return {}

    user = admincore.get_user_by_name(tlist['username'])
    guest = admincore.get_user_by_name(guest_name)
    relation = get_relation(user, guest)

    tlist['guest_privilege'] = privilege.get_privilege(tlist['privilege'], relation)

    if not privilege.has_privilege(tlist.guest_privilege, PRIVILEGE_CONTENT):
        tlist['title'] = None

    if not privilege.has_privilege(tlist.guest_privilege, PRIVILEGE_SHOWN):
        tlist = {}

    return tlist


def get_lists_of_user(user_name):
    tlists = ListCollection.find({'name': user_name})
    return tlists


def add_list_to_user(user, tlist, privilege):
    '''
    tlist = [['string', done],
             ['string2', done2]
             ...]
    '''
    tmp = dict(
        username=user['name'],
        list=tlist,
        privilege=privilege,
        display=1)

    return ListCollection.insert(tmp)


def eddit_list(lid, set_content):
    return ListCollection.find_and_modify(
        query={'_id': ObjectId(lid)},
        update={'$set': set_content},
        upsert=False, full_response=True)


def delete_list(lid):
    return eddit_list(lid, {'display': 0})


def share_a_list(guest_name, eid):
    try:
        tlist = CalCollection.find_one({'_id': ObjectId(eid)})
    except Exception, e:
        print 'in share_a_list: ', e
        return False

    user = admincore.get_user_by_name(tlist['username'])
    guest = admincore.get_user_by_name(guest_name)
    relation = get_relation(user, guest)

    tlist['guest_privilege'] = privilege.get_privilege(tlist['privilege'], relation)

    if not privilege.has_privilege(tlist.guest_privilege, PRIVILEGE_SHARE):
        return False
    else:
        res = add_list_to_user(tlist, guest)
        return res
