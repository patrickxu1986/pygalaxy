#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect
import logging
import os
import datetime
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory_path = project_dir + '/logs'
if not os.path.exists(log_directory_path):
    os.makedirs(log_directory_path)
print('LOGS DIR PATH: ' + log_directory_path)

now = datetime.datetime.now()
date_str = datetime.datetime.strftime(now, '%Y-%m-%d')
log_file = (str(log_directory_path) + '/' + date_str + '.log')

# pa = os.path.abspath(inspect.getframeinfo(inspect.stack()[-1][0])[0])
# pa = pa.split("/")[0: -1]
# pa = '/'.join(pa)
# print(pa)

# 创建文件和命令行的handler
s_handler = logging.StreamHandler()
f_handler = logging.FileHandler(log_file)
# 分别设置两个handler的日志等级，大于等于这个等级的才输出
s_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)
# 设置日志的输出格式并把格式添加到handler中
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
s_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)
# 把handler添加到logger对象中
logger.addHandler(f_handler)
logger.addHandler(s_handler)


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


if __name__ == '__main__':
    debug('logging')
    info('logging')
    warning('logging')
    error('logging')
