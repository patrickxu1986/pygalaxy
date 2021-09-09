#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql


class SQLMaster(object):

    def __init__(self, host: str, user: str, password: str, db: str, port: int = 3306):
        """
        初始化数据库连接
        :param host:           数据库主机地址
        :param user:           连接用户
        :param password:       连接密码
        :param db:             目标数据库
        :param port:           数据库连接端口，默认3306
        """
        try:
            self.db = db
            self.connection = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset='utf8')
            print('[SQLMaster] - mysql database [%s] connect success...' % db)
        except Exception as e:
            print('[SQLMaster] - mysql database [%s] connect failure...' % db)
            print(repr(e))

    def close(self):
        """
        关闭数据库连接
        """
        try:
            if self.connection:
                self.connection.close()
            print('[SQLMaster] - mysql database [%s] closed success...' % self.db)
        except Exception as e:
            print('[SQLMaster] - mysql database [%s] closed failure...' % self.db)
            print(repr(e))

    def execute(self, sql: str):
        """
        执行插入、修改、删除等操作
        :param sql:            sql语句
        :return:               返回执行是否成功的bool
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.connection.commit()
                print("[SQLMaster] - execute success... [%s]" % sql)
                return True
            except Exception as e:
                print("[SQLMaster] - execute failure... [%s]" % sql)
                print("[SQLMaster] - %s" % repr(e))
                return False
            finally:
                pass
                # if cursor:
                #     cursor.close()

    def fetch(self, sql: str):
        """
        执行结果查询操作
        :param sql:            sql语句
        :return:               查询成功返回结果元组，元组中的每一个item也是一个元组，读取数据时按index读取
                               例如：
                                    for row in rows:
                                        id = row[0]
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                result_rows = cursor.fetchall()
                if result_rows is None or len(result_rows) <= 0:
                    print("[SQLMaster] - execute failure... [%s] no result found" % sql)
                    return None
                print("[SQLMaster] - execute success... [%s]" % sql)
                return result_rows
            except Exception as e:
                print("[SQLMaster] - execute failure... [%s]" % sql)
                print("[SQLMaster] - %s" % repr(e))
                return None
            finally:
                pass
                # if cursor:
                #     cursor.close()


if __name__ == '__main__':
    connection = SQLMaster(host='localhost', user='root', password='xx', db='wiatec_movie')
    connection.execute('UPDATE m_video SET title = "1123" WHERE id = 2')
    connection.fetch(sql='SELECT * FROM m_video WHERE id > 0')
    connection.close()
