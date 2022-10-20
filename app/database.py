# -*- coding: utf-8 -*-
"""
@File    : database.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from peewee import SqliteDatabase
import logging

# 设置数据库
db = SqliteDatabase("demo.db")

# 打印日志
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
logger.propagate = False  # 不向上传播
