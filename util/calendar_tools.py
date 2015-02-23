#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import *
from config import *
import util.myTools as myTools 
from bson.objectid import ObjectId

RELATION_FRIEND = 1
RELATION_STRANGER = 0
PRIVILEGE_CONTENT = 8
PRIVILEGE_SHOWN = 4
PRIVILEGE_ATTEND = 2
PRIVILEGE_SHARE = 1

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

def get_relation(user, guest, res):
    '''
    res = 1 : Friend
    res = 0 : Stranger
    '''
    return res

def get_privilege(event, relation):
    if relation == RELATION_FRIEND:
        return event['privilege'] >> 4
    elif relation == RELATION_STRANGER:
        return event['privilege'] & 15
    else:
        return 0

def add_event_to_user(event, user):
    # cal = {}
    # cal['blabla'] = xxxx
    cal = {}
    cal['author'] = user['name']
    cal['title'] = user['title']
    cal['starttime'] = user['starttime']
    cal['endtime'] = user['endtime']
    cal['allday'] = user['allday']
    cal['privilege'] = user['privilege']
    CalCollection.insert(cal)
    return True

def get_host_of_event(event):
    user = myTools.get_user_by_id(event['hid'])
    return user


def get_event_by_id(eid, guest, rel):
    try:
        event = CalCollection.find_one({'_id': ObjectId(eid)})
    except Exception, e:
        print 'get_event_by_id: ', e
        return {}

    user = get_host_of_event(event)
    relation = get_relation(user, guest, rel) 

    event['guest_privilege'] = get_privilege(event, relation)

    if event.guest_privilege&PRIVILEGE_CONTENT != PRIVILEGE_CONTENT:
        event['title'] = None

    if event.guest_privilege&PRIVILEGE_SHOWN != PRIVILEGE_SHOWN:
        event = {}

    return event

def get_events_of_user(user):
    events = CalCollection.find({'name': user['name']})
    return events

def get_events_of_user_to_guest(user, guest, rel):
    relation = get_relation(user, guest, rel) 
    if relation == RELATION_FRIEND:
        pri = 64
    elif relation == RELATION_STRANGER:
        pri = 4
    else:
        pri = 255

    events = CalCollection.find_one({"author": user["name"]})
    for event in events:
        if event['privilege']&pri != pri:
            events.remove(event)

    return events

def share_a_event(guest, eid, rel):
    try:
        event = CalCollection.find_one({'_id': ObjectId(eid)})
    except Exception, e:
        print 'in share_a_event: ', e
        return False

    user = get_host_of_event(event)
    relation = get_relation(user, guest, rel)

    event['guest_privilege'] = get_privilege(event, relation)

    if event.guest_privilege&PRIVILEGE_SHARE != PRIVILEGE_SHARE:
        return False
    else:
        res = add_event_to_user(event, guest)
        return res
