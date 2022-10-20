# -*- coding: utf-8 -*-
"""
@File    : base_model.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from peewee import Model

from app.database import db


class BaseModel(Model):
    """
    # 基类，设置数据库链接
    """

    class Meta:
        database = db
