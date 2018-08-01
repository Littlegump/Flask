# _*_ coding: utf-8 _*_

import pymysql
import os, binascii


# 数据库的启动文件
conn_mysql_dict = dict(
    host='localhost',
    port=3306,
    user='testuser',
    password='testpwd',
    db='testdb',
    db2='testdb2',
    db3='testdb3',
    cursorclass=pymysql.cursors.DictCursor
)



# 一下是有关flask app的配置文件
run_flask_dict = dict(
    host='0.0.0.0',
    port=3333,
    debug=True
)


class ConfigBase():
    DEBUG = False
    #SECRET_KEY = binascii.hexlify(os.urandom(24))
    SECRET_KEY = binascii.hexlify(os.urandom(24))


class ConfigDevelopment(ConfigBase):
    """For development. Inherit from ConfigBase and override some values"""
    DEBUG = True

class ConfigProduction(ConfigBase):
    """For Production. Inherit from ConfigBase and override some values"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{host}:{port}/{db}".format(**conn_mysql_dict)
    DB2_URI = "mysql://{user}:{password}@{host}:{port}/{db2}".format(**conn_mysql_dict)
    DB3_URI = "mysql://{user}:{password}@{host}:{port}/{db3}".format(**conn_mysql_dict)
    print DB2_URI
    SQLALCHEMY_BINDS = {
        "db2": DB2_URI,
        "db3": DB3_URI
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = True
