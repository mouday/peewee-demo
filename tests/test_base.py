# -*- coding: utf-8 -*-
"""
@File    : test_insert.py
@Date    : 2022-10-19
@Author  : Peng Shiyu
"""
import unittest

from app.database import db


def dict_factory(cursor, row):
    """将返回结果转换为dict"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class TestBase(unittest.TestCase):

    # 所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        """
        链接数据库
        """
        db.connect()

    # 所有test运行完后运行一次
    @classmethod
    def tearDownClass(cls):
        """
        断开数据库
        """
        if not db.is_closed():
            db.close()

    def test_execute_sql_fetchall(self):
        """
        执行原生sql
        """
        cursor = db.execute_sql("select * from tb_user where id = ?", (1,))
        rows = cursor.fetchall()
        print(rows)
        # [(1, 'Jack', 23, '2022-10-19 18:09:07.038935', '2022-10-19 18:09:07.038940')]

    def test_execute_sql_fetchone(self):
        """
        执行原生sql
        """
        cursor = db.execute_sql("select * from tb_user where id = ?", (1,))

        # 将返回结果转换为dict
        cursor.row_factory = dict_factory
        row = cursor.fetchone()
        print(row)
        # {'id': 1, 'name': 'Jack', 'age': 23, 'created_time': '2022-10-19 18:09:07.038935', 'update_time': '2022-10-19 18:09:07.038940'}
