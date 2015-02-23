#!/usr/bin/env python
#encoding=utf-8

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model import *
import torndb

def installUsersTable():
    CalendarDatabase.reconnect()
    CalendarDatabase.execute("""CREATE TABLE `usersTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(64) NOT NULL,
            `name` VARCHAR(32) NOT NULL,
            `password` VARCHAR(512) NOT NULL,
            `last_login` timestamp,
            `admin` TINYINT(1) DEFAULT '0',
            `checked` TINYINT(1) DEFAULT '0',
            `subscribed` TINYINT(1) DEFAULT '1',
            `ext` VARCHAR(10),
            PRIMARY KEY(id),
            UNIQUE KEY`name`(`name`),
            UNIQUE KEY`email`(`email`))
            AUTO_INCREMENT=100000
            DEFAULT CHARSET=utf8
    """)

def installFllwTable():
    CalendarDatabase.reconnect()
    CalendarDatabase.execute("""CREATE TABLE `fllwTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `pid` VARCHAR(64) NOT NULL,
            `fid` VARCHAR(32) NOT NULL,
            `fllw_time` timestamp,
            `checked` TINYINT(1) DEFAULT '0',
            PRIMARY KEY(id))
            DEFAULT CHARSET=utf8
    """)

def installCheckTable():
    CalendarDatabase.reconnect()
    CalendarDatabase.execute("""CREATE TABLE `checkTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(64) NOT NULL,
            `code` VARCHAR(64) NOT NULL,
            `check_time` timestamp,
            `checked` TINYINT(1) DEFAULT '0',
            PRIMARY KEY(id))
            DEFAULT CHARSET=utf8
    """)

def installCalendarTable():
    CalendarDatabase.reconnect()
    CalendarDatabase.execute('''CREATE TABLE `calendarTable`(
        `id` INT NOT NULL AUTO_INCREMENT,
        `hid` INT NOT NULL,
        `title` text,
        `starttime` timestamp,
        `endtime` timestamp DEFAULT '0000-00-00 00:00:00',
        `allday` int,
        `privilege` int,
        PRIMARY KEY(id))
        DEFAULT CHARSET=utf8
    ''')

def installSaltingTable():
    CalendarDatabase.reconnect()
    CalendarDatabase.execute("""CREATE TABLE `saltTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(64) NOT NULL,
            `name` VARCHAR(32) NOT NULL,
            `salt` VARCHAR(64) NOT NULL,
            PRIMARY KEY(id))
            DEFAULT CHARSET=utf8
    """)

if __name__ == "__main__":
    # db.init_db()
    # models.kv.db_inited = ''
    print sys.argv

    if '-U' in sys.argv or '-A' in sys.argv:
        installUsersTable()

    if '-F' in sys.argv or '-A' in sys.argv:
        installFllwTable()
        
    if '-C' in sys.argv or '-A' in sys.argv:
        installCalendarTable()

    if '-CHECK' in sys.argv or '-A' in sys.argv:
        installCheckTable()

    if '-SALT'in sys.argv or '-A' in sys.argv:
        installSaltingTable()
