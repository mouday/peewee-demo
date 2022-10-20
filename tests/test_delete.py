# -*- coding: utf-8 -*-
"""
@File    : test_insert.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from tests.test_base import TestBase
from app.model.user_model import UserModel


class TestDelete(TestBase):
    """
    删除数据
    """
    def test_delete_by_id(self):
        """
        按照主键删除
        """
        user = UserModel.get_or_none(UserModel.name == 'Tom')
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ? OFFSET ?', ['Tom', 1, 0])

        UserModel.delete_by_id(user.id)
        #  ('DELETE FROM "tb_user" WHERE ("tb_user"."id" = ?)', [1])

    def test_delete_instance(self):
        """
        删除实例
        """
        user = UserModel.get(UserModel.name == 'Tom')
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ? OFFSET ?', ['Tom', 1, 0])

        user.delete_instance()
        # ('DELETE FROM "tb_user" WHERE ("tb_user"."id" = ?)', [4])

    def test_delete(self):
        """
        按条件删除
        """
        user = UserModel.get(UserModel.name == 'Tom')
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ? OFFSET ?', ['Tom', 1, 0])

        UserModel.delete().where(
            UserModel.id == user.id
        ).execute()
        # ('DELETE FROM "tb_user" WHERE ("tb_user"."id" = ?)', [5])

    def test_truncate_table(self):
        """
        清空表数据
        """
        UserModel.truncate_table()
        # ('DELETE FROM "tb_user"', [])
