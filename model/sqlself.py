# _*_ coding: utf-8 _*__

from config.config import conn_mysql_dict
from utility.mysqlHelper import mysqlHelper
import pymysql

class sqlSelf(object):
    def __init__(self):
        self.__helper = mysqlHelper()

    def get_db_version(self):
        version_sql = "SELECT VERSION()"
        return self.__helper.get_db_version(version_sql)

    def getOne(self,params):
        sql  = "select * from cafe where price > %s"
        return self.__helper.getOne(sql,params)

    def insertIterm(self, params):
        #sql = """insert into cafe (category, name, price) values (%s, %s, %s)"""
        sql = 'insert into cafe (category, name, price) values (%s, %s, %s)'
        print sql, params

        rslt = self.__helper.insertIterm(sql, params)
        return "rslt is : %s" % rslt
