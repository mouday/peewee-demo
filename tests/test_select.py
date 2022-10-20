# -*- coding: utf-8 -*-
"""
@File    : test_insert.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from tests.test_base import TestBase
from app.model.user_model import UserModel


class TestSelect(TestBase):
    """
    取数据
    """
    def test_select_get(self):
        """
        条件查询一条
        """
        row = UserModel.select().where(
            UserModel.name == 'Tom'
        ).get()

        print(row)
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ? OFFSET ?', ['Tom', 1, 0])

    def test_select_first(self):
        """
        获取第一条
        """
        row = UserModel.select().where(
            UserModel.name == 'Tom'
        ).first()

        print(row)
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ?', ['Tom', 1])

    def test_get(self):
        """
        通过获取，不存在报错
        """
        row = UserModel.get(UserModel.name == 'Tom')
        print(row)
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ? OFFSET ?', ['Tom', 1, 0])

    def test_get_or_none(self):
        """
        通过获取或者返回None
        """
        user = UserModel.get_or_none(UserModel.name == 'Jack')
        print(user)
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) LIMIT ? OFFSET ?', ['Jack', 1, 0])

    def test_get_by_id(self):
        """
        通过主键获取，不存在报错
        """
        user = UserModel.get_by_id(1)
        print(user)
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."id" = ?) LIMIT ? OFFSET ?', [1, 1, 0])

    def test_get_or_create(self):
        """
        获取或创建
        """
        UserModel.get_or_create(name='Tom', age=23)
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE (("t1"."name" = ?) AND ("t1"."age" = ?)) LIMIT ? OFFSET ?', ['Tom', 23, 1, 0])
        # ('BEGIN', None)
        # ('INSERT INTO "tb_user" ("name", "age", "created_time", "update_time") VALUES (?, ?, ?, ?)', ['Tom', 23, datetime.datetime(2022, 10, 19, 18, 9, 7, 38935), datetime.datetime(2022, 10, 19, 18, 9, 7, 38940)])

    def test_select(self):
        """
        查询多条记录
        注意，获取的是 iterator
        可以转为 namedtuples(), tuples(), dicts()
        """
        query = UserModel.select().where(
            UserModel.name == 'Tom'
        )

        print(list(query))
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?)', ['Tom'])

        # [<UserModel: 1>]

    def test_select_order(self):
        """
        排序
        """
        query = UserModel.select().where(
            UserModel.name == 'Tom'
        ).order_by(UserModel.age.desc())

        print(list(query))
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" WHERE ("t1"."name" = ?) ORDER BY "t1"."age" DESC', ['Tom'])

        # [<UserModel: 1>]

    def test_select_paginate(self):
        """
        分页
        """
        query = UserModel.select().paginate(2, 10)
        print(list(query))
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" LIMIT ? OFFSET ?', [10, 10])

    def test_select_count(self):
        """
        统计
        """

        query = UserModel.select().count()
        print(list(query))
        # ('SELECT COUNT(1) FROM (SELECT 1 FROM "tb_user" AS "t1") AS "_wrapped"', [])

    def test_select_group(self):
        """
        分组
        """
        query = UserModel.select().group_by(UserModel.name)

        print(list(query))
        # ('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" FROM "tb_user" AS "t1" GROUP BY "t1"."name"', [])
