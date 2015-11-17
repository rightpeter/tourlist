#!/usr/bin/env python
#encoding=utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

tourlistdb = client.tourlist

UserCollection = tourlistdb.user
# id unique
# email string unique
# name string unique
# password VARCHAR(512)
# last_login timestamp
# salt VARCHAR(64)
ListCollection = tourlistdb.tlist
# id unique
# username -> user.name
# tlist -> []
#     tlist = [['string', done],
#              ['string2', done2]
#              ...
# privilege int
# display int
