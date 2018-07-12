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
    SQLALCHEMY_TRACK_MODIFICATIONS = True
