# -*- coding: utf-8 -*-
"""
@File    : test_insert.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from tests.test_base import TestBase
from app.model.user_model import UserModel


class TestTable(TestBase):
    """
    表操作
    """

    def test_create_table(self):
        """
        建表
        """
        UserModel.create_table()
        #  ('CREATE TABLE IF NOT EXISTS "tb_user" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "age" INTEGER NOT NULL, "created_time" DATETIME NOT NULL, "update_time" DATETIME NOT NULL)', [])

    def test_table_exists(self):
        """
        查看表是否存在
        """
        ret = UserModel.table_exists()
        print(ret)
        # ('SELECT name FROM "main".sqlite_master WHERE type=? ORDER BY name', ('table',))

    def test_drop_table(self):
        """
        删除表
        """
        UserModel.drop_table()
#         ('DROP TABLE IF EXISTS "tb_user"', [])
