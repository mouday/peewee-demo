# -*- coding: utf-8 -*-
"""
@File    : user_model.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from datetime import datetime

from peewee import CharField, DateTimeField, IntegerField, AutoField

from app.model.base_model import BaseModel


class UserModel(BaseModel):
    """
    用户表
    """

    id = AutoField()
    name = CharField(null=False)
    age = IntegerField(null=False)

    created_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'tb_user'
