#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import util.myTools as myTools
import util.calendar_tools as calendar_tools

def test_share_a_event():
    rel = int(raw_input('Input the rel of guest: \n'))
    user = myTools.get_user_by_name('Rightpeter')
    guest = myTools.get_user_by_name('june_fiend')
    events = calendar_tools.get_events_of_user_to_guest(user, guest, rel)
    print 'events: ', events
    for event in events:
        event_info = calendar_tools.get_event_by_id(event['id'], guest, rel)
        try:
            print 'id: ', event_info.id, ' title: ', event_info.title, ' privilege: ', event_info.privilege
        except Exception, e:
            print e
            print 'None'

    eid = int(raw_input('Input the ID of event: \n'))
    res = calendar_tools.share_a_event(guest, eid, rel)
    print res
    events = calendar_tools.get_events_of_user(guest)
    for event in events:
        event_info = calendar_tools.get_event_by_id(event['id'], guest, rel)
        try:
            print 'id: ', event_info.id, ' title: ', event_info.title, ' privilege: ', event_info.privilege, ' guest_privilege: ', event_info.guest_privilege
        except Exception, e:
            print e

if __name__ == '__main__':
    test_share_a_event()
