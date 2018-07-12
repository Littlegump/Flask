# _*_ coding: utf-8 _*__

import os
import pymysql
from config.config import conn_mysql_dict
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class mysqlHelper(object):
    def __init__(self):
        #self.__conn = pymysql.connect(**conn_mysql_dict)
        self.__conn = conn_mysql_dict

    def get_db_version(self, sql, params=("")):
        conn = pymysql.connect(**self.__conn)
        cursor = conn.cursor()
        print "cursor has been gotten."
        cursor.execute(sql)
        version = cursor.fetchone()
        print('Database version : %s ' % version)
        cursor.close()
        conn.close()
        return version

    def getDict(self, sql, params=""):
        conn = pymysql.connect(**self.__conn)
        with conn.cursor() as cursor:
            reCount = cursor.execute(sql, params)
            rslt = cursor.fetchall()
        conn.close()
        return rslt

    def getOne(self, sql, params=""):
        conn = pymysql.connect(**self.__conn)
        with conn.cursor() as cursor:
            reCount = cursor.execute(sql, params)
            rslt = cursor.fetchone()
        conn.close()
        return rslt

    def insertIterm(self, sql, params):
        try:
            conn = pymysql.connect(**self.__conn)
            with conn.cursor() as cursor:
                cursor.executemany(sql, params)
                conn.commit()
            with conn.cursor() as cursor:
                sql = "SELECT * FROM cafe"
                cursor.execute(sql)
                rslt = cursor.fetchall()
        finally:
            conn.close()
        return rslt

#helper = mysqlHelper()
#sql = "select * from cafe where price > %s"
#params = (str(0.12),)
#a = helper.getOne(sql, params)
#ba = helper.getDict(sql, params)
#print a
#
#print ba

#a = mysqlHelper()
#c = a.get_db_version()
#print c
