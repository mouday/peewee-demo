# Python：peewee常用操作CURD

Defining models is similar to Django or SQLAlchemy

>译文：定义模型类似于Django或SQLAlchemy

## 目录

- 1、数据库 Database
    - 1.1、设置参数
    - 1.2、连接数据库
    - 1.3、执行原生sql
- 2、模型 Model
    - 2.1、定义模型
    - 2.2、表操作
- 3、模型的CURD操作
    - 3.1、写入操作
    - 3.2、更新数据
    - 3.3、删除数据
    - 3.4、取单条数据
    - 3.5、取多条数据

文档
- github： [https://github.com/coleifer/peewee](https://github.com/coleifer/peewee)
- 官方文档：[http://docs.peewee-orm.com/](http://docs.peewee-orm.com/)
-  pypi [https://pypi.org/project/peewee/](https://pypi.org/project/peewee/)

示例代码仓库

[https://github.com/mouday/peewee-demo](https://github.com/mouday/peewee-demo)

安装

```
pip install peewee
```

测试环境

```bash
$ python --version
Python 3.7.0

$ pip show peewee
Name: peewee
Version: 3.15.3
```

## 1、数据库 Database

### 1.1、设置参数

```python
# -*- coding: utf-8 -*-
"""
@File    : database.py
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

```

### 1.2、连接数据库

```python
from app.database import db

# 链接数据库
db.connect()

# 断开数据库
if not db.is_closed():
    db.close()
    
```

### 1.3、执行原生sql

获取多条记录

```python
cursor = db.execute_sql("select * from tb_user where id = ?", (1,))
rows = cursor.fetchall()
print(rows)
```

```python
[
    (1, 'Jack', 23, '2022-10-19 18:09:07.038935', '2022-10-19 18:09:07.038940')
]
```

获取单条记录

```python
cursor = db.execute_sql("select * from tb_user where id = ?", (1,))

# 将返回结果转换为dict
# https://docs.python.org/zh-cn/3.6/library/sqlite3.html#sqlite3.Connection.row_factory 
def dict_factory(cursor, row):
    """将返回结果转换为dict"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

cursor.row_factory = dict_factory
row = cursor.fetchone()
print(row)
```

```python
{
    'id': 1, 
    'name': 'Jack', 
    'age': 23, 
    'created_time': '2022-10-19 18:09:07.038935', 
    'update_time': '2022-10-19 18:09:07.038940'
}
```

## 2、模型 Model

### 2.1、定义模型

定义基类模型

```python
# -*- coding: utf-8 -*-
"""
@File    : base_model.py
"""

from peewee import Model

from app.database import db


class BaseModel(Model):
    """
    # 基类，设置数据库链接
    """

    class Meta:
        database = db

```

定义模型

```python
# -*- coding: utf-8 -*-
"""
@File    : user_model.py
"""

from datetime import datetime

from peewee import CharField, DateTimeField, IntegerField

from app.model.base_model import BaseModel


class UserModel(BaseModel):
    """
    用户表
    """

    id = IntegerField(primary_key=True)
    name = CharField(null=False)
    age = IntegerField(null=False)

    created_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.now)

    class Meta:
        # 指定表名
        table_name = 'tb_user'

```

### 2.2、表操作

建表

```python
UserModel.create_table()
```

```sql
(
    'CREATE TABLE IF NOT EXISTS "tb_user" (
    "id" INTEGER NOT NULL PRIMARY KEY, 
    "name" VARCHAR(255) NOT NULL, 
    "age" INTEGER NOT NULL, 
    "created_time" DATETIME NOT NULL, 
    "update_time" DATETIME NOT NULL)', 
    []
)
```

查看表是否存在
```python
UserModel.table_exists()
```

```sql
(
    'SELECT name FROM "main".sqlite_master WHERE type=? ORDER BY name',
    ('table',)
 )
```

删除表

```python
UserModel.drop_table()
```

```sql
(
    'DROP TABLE IF EXISTS "tb_user"', 
    []
)
```


## 3、模型的CURD操作

### 3.1、写入操作

插入数据

```python
ret = UserModel.insert({
    UserModel.age: 20,
    UserModel.name: 'Tom'
}).execute()
```

```sql
'INSERT INTO "tb_user"
("name", "age", "created_time", "update_time")
VALUES (?, ?, ?, ?)',
[
    'Tom', 
    20, 
    datetime.datetime(2022, 10, 19, 17, 28, 30, 198981), 
    datetime.datetime(2022, 10, 19, 17, 28, 30, 198988)
]

```

插入字典数据

```python
ret = UserModel.insert({
    'age': 20,
    'name': 'Tom'
}).execute()
```

```sql
'INSERT INTO "tb_user"
("name", "age", "created_time", "update_time")
VALUES (?, ?, ?, ?)',
[
    'Tom', 
    20, 
    datetime.datetime(2022, 10, 19, 17, 28, 30, 198981), 
    datetime.datetime(2022, 10, 19, 17, 28, 30, 198988)
]
```

保存实例

```python
user = UserModel(
    age=21,
    name='Tom'
)

user.save()
```

```sql
('INSERT INTO "tb_user" 
    ("name", "age", "created_time", "update_time") 
    VALUES (?, ?, ?, ?)', 
['Charlie', 12, 
datetime.datetime(2022, 10, 19, 17, 34, 43, 376650), 
datetime.datetime(2022, 10, 19, 17, 34, 43, 376652)])
```


插入并创建实例

```python
user = UserModel.create(
    age=22,
    name='Tom'
)
```

```sql
('INSERT INTO "tb_user" 
    ("name", "age", "created_time", "update_time") 
    VALUES (?, ?, ?, ?)', 
    ['Charlie', 12, 
    datetime.datetime(2022, 10, 19, 17, 36, 16, 408224), 
    datetime.datetime(2022, 10, 19, 17, 36, 16, 408226)])
```

插入多条数据

```python
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
```

```sql
('INSERT INTO "tb_user" 
    ("name", "age", "created_time", "update_time") 
    VALUES (?, ?, ?, ?), (?, ?, ?, ?)', 
    [
    'Tom', 23, 
    datetime.datetime(2022, 10, 19, 17, 38, 48, 106336), 
    datetime.datetime(2022, 10, 19, 17, 38, 48, 106344), 
    'Tom', 24, 
    datetime.datetime(2022, 10, 19, 17, 38, 48, 106355), 
    datetime.datetime(2022, 10, 19, 17, 38, 48, 106360)])
```

### 3.2、更新数据

更新多条数据

```python
UserModel.update(
    name='Jack'
).where(
    UserModel.id == 1
).execute()
```

```sql
('UPDATE "tb_user" SET "name" = ? WHERE ("tb_user"."id" = ?)', ['Jack', 1])
```

更新单条数据

```python
UserModel.set_by_id(1, {'name': 'Jack'})
```

```sql
('UPDATE "tb_user" SET "name" = ? WHERE ("tb_user"."id" = ?)', ['Jack', 1])
```


### 3.3、删除数据


按照主键删除

```python
UserModel.delete_by_id(1)
```

```sql
('DELETE FROM "tb_user" WHERE ("tb_user"."id" = ?)', [1])
```

按条件删除

```python
UserModel.delete().where(
    UserModel.id == 1
).execute()
```

```sql
('DELETE FROM "tb_user" WHERE ("tb_user"."id" = ?)', [1])
```


删除实例

```python
user = UserModel.get_by_id(1)
       
user.delete_instance()
```

```sql
('DELETE FROM "tb_user" WHERE ("tb_user"."id" = ?)', [1])
```


清空表数据

```python
UserModel.truncate_table()
```

```sql
('DELETE FROM "tb_user"', [])
```

### 3.4、取单条数据

条件查询一条

```python
row = UserModel.select().where(
    UserModel.name == 'Tom'
).get()

print(row)
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."name" = ?) 
    LIMIT ? OFFSET ?', 
    ['Tom', 1, 0])
```

获取第一条

```python
row = UserModel.select().where(
    UserModel.name == 'Tom'
).first()

print(row)
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."name" = ?) 
    LIMIT ?', 
    ['Tom', 1])
```

通过获取，不存在报错

```python
row = UserModel.get(UserModel.name == 'Tom')
print(row)
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."name" = ?) 
    LIMIT ? OFFSET ?', 
    ['Tom', 1, 0])
```

通过获取或者返回None


```python
user = UserModel.get_or_none(UserModel.name == 'Jack')
print(user)
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."name" = ?) 
    LIMIT ? OFFSET ?', 
    ['Jack', 1, 0])
```

通过主键获取，不存在报错

```python
user = UserModel.get_by_id(1)

print(user)
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."id" = ?) 
    LIMIT ? 
    OFFSET ?', 
    [1, 1, 0])
```

获取或创建

```python
UserModel.get_or_create(name='Tom', age=23)
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE (("t1"."name" = ?) AND ("t1"."age" = ?)) 
    LIMIT ? OFFSET ?', 
    ['Tom', 23, 1, 0])

('BEGIN', None)

('INSERT INTO "tb_user" 
    ("name", "age", "created_time", "update_time") 
    VALUES (?, ?, ?, ?)', 
    ['Tom', 23, 
    datetime.datetime(2022, 10, 19, 18, 9, 7, 38935), 
    datetime.datetime(2022, 10, 19, 18, 9, 7, 38940)])
```

### 3.5、取多条数据


查询多条记录

```python
# 注意，获取的是 iterator
# 可以转为 namedtuples(), tuples(), dicts()

query = UserModel.select().where(
    UserModel.name == 'Tom'
)

print(list(query))
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."name" = ?)', 
    ['Tom'])
```

排序

```python
query = UserModel.select().where(
    UserModel.name == 'Tom'
).order_by(UserModel.age.desc())

print(list(query))
# [<UserModel: 1>]
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    WHERE ("t1"."name" = ?) 
    ORDER BY "t1"."age" DESC', 
    ['Tom'])
```

分页

```python
query = UserModel.select().paginate(2, 10)

print(list(query))
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    LIMIT ? OFFSET ?', 
    [10, 10])
```

统计

```python
query = UserModel.select().count()
print(list(query))
```

```sql
('SELECT COUNT(1) FROM (SELECT 1 FROM "tb_user" AS "t1") AS "_wrapped"', [])
```

分组

```python
query = UserModel.select().group_by(UserModel.name)

print(list(query))
```

```sql
('SELECT "t1"."id", "t1"."name", "t1"."age", "t1"."created_time", "t1"."update_time" 
    FROM "tb_user" AS "t1" 
    GROUP BY "t1"."name"', 
    [])
```

