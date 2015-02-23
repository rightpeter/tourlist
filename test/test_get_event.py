#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import util.myTools as myTools
import util.calendar_tools as calendar_tools

def test_get_events():
    print '------------ test_get_events -------------'
    user = myTools.get_user_by_name('Rightpeter')
    events = calendar_tools.get_events_of_user(user)
    for event in events:
        event_info = calendar_tools.get_event_by_id(event['id'], user, 1)
        print 'title: ', event_info['title'], ' privilege: ', event_info['privilege']

def test_get_events_to_friend():
    print '------------ test_get_events_to_guest ----------'
    user = myTools.get_user_by_name('Rightpeter') 
    guest = myTools.get_user_by_name('june_fiend')
    events = calendar_tools.get_events_of_user_to_guest(user, guest, 1)
    for event in events:
        event_info = calendar_tools.get_event_by_id(event['id'], guest, 1)
        print 'title: ', event_info['title'], ' privilege: ', event_info['privilege']

def test_get_events_to_stranger():
    print '------------ test_get_events_to_guest ----------'
    user = myTools.get_user_by_name('Rightpeter') 
    guest = myTools.get_user_by_name('june_fiend')
    events = calendar_tools.get_events_of_user_to_guest(user, guest, 0)
    for event in events:
        event_info = calendar_tools.get_event_by_id(event['id'], guest, 0)
        print 'title: ', event_info['title'], ' privilege: ', event_info['privilege']

if __name__ == '__main__':
    test_get_events()
    test_get_events_to_friend()
    test_get_events_to_stranger()
