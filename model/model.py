#!/usr/bin/env python
#encoding=utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

CalendarDB = client.SocialCal

UserCollection = CalendarDB.user
SaltCollection = CalendarDB.salt
CalCollection = CalendarDB.calendar
