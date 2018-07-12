#! _*_ coding: utf-8 _*_

from utility import mysqlHelper

class Admin(object):
    """docstring for ."""
    def __init__(self):
        self.__helper = mysqlHelper()

    def getOne(self):
        sql = "select * from cafe where name=%s"
        params = ("Cappuccino",)
        return self.__helper.getOne(sql, params)
