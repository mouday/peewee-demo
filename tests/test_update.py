# -*- coding: utf-8 -*-
"""
@File    : test_insert.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from tests.test_base import TestBase
from app.model.user_model import UserModel


class TestUpdate(TestBase):
    """
    更新数据
    """

    def test_update(self):
        """
        更新多条数据
        """
        UserModel.update(
            name='Jack'
        ).where(
            UserModel.id == 1
        ).execute()

        # ('UPDATE "tb_user" SET "name" = ? WHERE ("tb_user"."id" = ?)', ['Jack', 1])


    def test_set_by_id(self):
        """
        更新单条数据
        """
        UserModel.set_by_id(1, {'name': 'Jack'})
        # ('UPDATE "tb_user" SET "name" = ? WHERE ("tb_user"."id" = ?)', ['Jack', 1])