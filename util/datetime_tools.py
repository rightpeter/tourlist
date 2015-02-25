# -*- coding: utf-8 -*-

import datetime
import time

datetime_format = '%Y-%m-%d %H:%M:%S'
date_format = '%Y-%m-%d'


def date_to_begin_end_time(date):
    '''
    date: datetime.datetime
    '''
    begin_time = datetime.datetime(date.year, date.month, date.day, 0, 0, 0)
    end_time = datetime.datetime(date.year, date.month, date.day, 23, 59, 59, 999)
    return begin_time, end_time


def date_to_string(date):
    return date.strftime(datetime_format)


def datetime_to_string(datetime):
    return datetime.strftime(datetime_format)


def string_to_date(string):
    string += " 0:0:0"
    time = datetime.datetime.strptime(string, datetime_format)
    return time.date()


def string_to_datetime(string):
    return datetime.datetime.strptime(string, datetime_format)


def string_to_timestamp(strTime):
    return time.mktime(string_to_datetime(strTime).timetuple())


def timestamp_to_string(stamp):
    return time.strftime(datetime_format, tiem.localtime(stamp))


def datetime_to_timestamp(dateTim):
    return time.mktime(dateTim.timetuple())


def datetime_change_zone(time, delta):
    delta = datetime.timedelta(hours=delta)
    return time + delta


def string_change_zone(time, delta):
    time = string_to_datetime(time)
    time = datetime_change_zone(time, delta)
    return datetime_to_string(time)
