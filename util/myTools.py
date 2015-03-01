#!/usr/bin/env python

# -*- coding: utf-8 -*-

from datetime import datetime

import hashlib
import uuid
from random import choice
import re
import time
import json
import tornado
import httplib
from email.mime.text import MIMEText
from model import *
from config import *
import traceback


def generate_password(passwd_length, passwd_seed):
    passwd = []
    while len(passwd) < passwd_length:
        passwd.append(choice(passwd_seed))
    return ''.join(passwd)


def get_json(domain, url):
    try:
        httpClient = httplib.HTTPConnection(domain, 8000, timeout=2000)
        httpClient.request('GET', url)

        response = httpClient.getresponse()
        response.reason
        return response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


def is_email(email):
    re_email = r'^([[a-zA-Z0-9]+[_|\_|\.]?]*[a-zA-Z0-9]+)@([[a-zA-Z0-9]+[_|\_|\.]?]*[a-zA-Z0-9]+)\.[a-zA-Z]{2,4}$'
    return bool(re.match(re_email, email, re.VERBOSE))


def get_hashed_password(password, salt):
    return hashlib.sha512(password + salt).hexdigest()


def get_random_salt():
    return uuid.uuid4().hex


def change_passwd(email, passwd, new_passwd, re_new_passwd):
    user = UserCollection.find_one({'email': email})
    if login(email, passwd) and new_passwd == re_new_passwd:
        passwd = new_passwd
        salt = uuid.uuid4().hex
        hashed_passwd = hashlib.sha512(passwd + salt).hexdigest()

        UserCollection.find_and_modify(
            query={'email': email},
            update={'$set': {'password': hashed_passwd, 'salt': salt}},
            upsert=False, full_response=True)
        return True
    else:
        return False


def change_name(name, new_name):
    if new_name and not is_name_exist(new_name):
        UserCollection.find_and_modify(
            query={'name': name},
            update={'$set': {'name': new_name}}, upsert=False,
            full_response=True)
        return True
    return False
