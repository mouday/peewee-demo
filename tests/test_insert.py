# -*- coding: utf-8 -*-
"""
@File    : test_insert.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""

from tests.test_base import TestBase
from app.model.user_model import UserModel


class TestInsert(TestBase):
    """
    插入数据
    """
    def test_insert(self):
        """
        插入数据
        """

        ret = UserModel.insert({
            UserModel.age: 20,
            UserModel.name: 'Tom'
        }).execute()

        # 'INSERT INTO "tb_user"
        # ("name", "age", "created_time", "update_time")
        # VALUES (?, ?, ?, ?)',
        # ['Tom', 20, datetime.datetime(2022, 10, 19, 17, 28, 30, 198981), datetime.datetime(2022, 10, 19, 17, 28, 30, 198988)]

        print(ret)
        # 1

    def test_insert_dict(self):
        """
        插入字典数据
        """
        ret = UserModel.insert({
            'age': 20,
            'name': 'Tom'
        }).execute()

        # 'INSERT INTO "tb_user"
        # ("name", "age", "created_time", "update_time")
        # VALUES (?, ?, ?, ?)',
        # ['Tom', 20, datetime.datetime(2022, 10, 19, 17, 28, 30, 198981), datetime.datetime(2022, 10, 19, 17, 28, 30, 198988)]

        print(ret)
        # 1

    def test_save(self):
        """
        保存实例
        """
        user = UserModel(
            age=21,
            name='Tom'
        )

        user.save()

    # ('INSERT INTO "tb_user" ("name", "age", "created_time", "update_time") VALUES (?, ?, ?, ?)', ['Charlie', 12, datetime.datetime(2022, 10, 19, 17, 34, 43, 376650), datetime.datetime(2022, 10, 19, 17, 34, 43, 376652)])

    def test_create(self):
        """
        插入并创建实例
        """
        user = UserModel.create(
            age=22,
            name='Tom'
        )

        print(user)

    #  ('INSERT INTO "tb_user" ("name", "age", "created_time", "update_time") VALUES (?, ?, ?, ?)', ['Charlie', 12, datetime.datetime(2022, 10, 19, 17, 36, 16, 408224), datetime.datetime(2022, 10, 19, 17, 36, 16, 408226)])

    def test_insert_many(self):
        """
        插入多条数据
        """
        UserModel.insert_many([
            {
                'age': 23,
                'name': 'Tom'
            },
            {
                'age': 24,
                'name': 'Tom'
            }
        ]).execute()
    # ('INSERT INTO "tb_user" ("name", "age", "created_time", "update_time") VALUES (?, ?, ?, ?), (?, ?, ?, ?)', ['Tom', 23, datetime.datetime(2022, 10, 19, 17, 38, 48, 106336), datetime.datetime(2022, 10, 19, 17, 38, 48, 106344), 'Tom', 24, datetime.datetime(2022, 10, 19, 17, 38, 48, 106355), datetime.datetime(2022, 10, 19, 17, 38, 48, 106360)])
