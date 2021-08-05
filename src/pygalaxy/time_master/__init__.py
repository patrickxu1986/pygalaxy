#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time


def get_current_date_str():
    now = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now, '%Y-%m-%d')
    return time_str


def get_current_time_str():
    now = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    return time_str


def get_current_unix_time():
    now = datetime.datetime.now()
    unix_time = time.mktime(now.timetuple())
    return int(unix_time)


if __name__ == '__main__':
    print(get_current_time_str())
    print(get_current_unix_time())
