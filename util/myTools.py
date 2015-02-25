#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import *
from datetime import datetime

import hashlib
import uuid
from random import choice
# import re
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


def is_email_exist(email):
    if is_email(email):
        user = UserCollection.find_one({'email': email})
        if user:
            return True
        else:
            return False


def is_name_exist(name):
    user = UserCollection.find_one({'name': name})

    if len(user):
        return True
    else:
        return False


def insert_a_user(user):
    '''
    user = {
        'email': 'xxx@xx.xx',
        'name': 'xxxx',
        'password': 'xxxx',
        }
    '''
    passwd = user['password']
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(passwd + salt).hexdigest()

    try:
        user['password'] = hashed_password
        user['salt'] = salt
        UserCollection.insert(user)
        return True
    except Exception, e:
        print traceback.print_exc()
        return False


def login(email, password):
    if not is_email_exist(email):
        user = UserCollection.find_one({'email': email})
        saved_password = user['password']
        salt = user['salt']
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        if hashed_password == saved_password:
            UserCollection.find_and_modify(
                query={'email': email},
                update={'$set': {'last_login': datetime.utcnow()}},
                upsert=False, full_response=True)
            name = user['name']
            print "email: ", email
            print "name", name
            return True
    return False


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
