#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time

DATE_FORMAT = '%Y-%m-%d'
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_current_date_str():
    """
    格式化获取当前的日期
    """
    now = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now, DATE_FORMAT)
    return time_str


def get_current_time_str():
    """
    格式化获取当前的日期时间
    """
    now = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now, DATE_TIME_FORMAT)
    return time_str


def get_current_unix_time():
    """
    获取当前10位unix时间戳
    """
    now = datetime.datetime.now()
    unix_time = time.mktime(now.timetuple())
    return int(unix_time)


if __name__ == '__main__':
    print(get_current_date_str())
    print(get_current_time_str())
    print(get_current_unix_time())
