import pymysql


class PymysqlPython(object):
    def __init__(self):
        # 这里为了简便，共用一个数据库连接，实际项目中应该对每个操作提供一个连接，或者做一个连接池
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='aizhan')
        self.select_list = []

    """
    普通查询
    """
    def select(self):
        # 普通游标，查询得到的数据默认为元组
        cursor = self.conn.cursor()

        select_sql = "select `domain`,`html` from aizhan2_copy"
        # select_sql = "select house_title from `wiwj_sh_ershoufang` where id>100"
        try:
            cursor.execute(select_sql)
            # 查询一条
            # row_1 = cursor.fetchone()
            # 查询9条
            # row_n = cursor.fetchmany(9)
            # 查询全部
            rows = cursor.fetchall()
            for row in rows:
                print(row[1])
                # 这里可以对查询到的数据进行一定的操作 例如，将查询的数据格式化为字典，然后存入列表(编数据过大则不建议使用，占内存)
                d = {'id': row[1]}
                self.select_list.append(d)
            self.conn.commit()
        except Exception as e:
            print('查询错误', e)
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    """
    流式游标查询
    """
    def select_ssdictcursor(self):
        # 流式字典游标 用于读取大表，避免占用大量内存 详见 mysql_python.md
        cursor = self.conn.cursor(cursor=pymysql.cursors.SSDictCursor)

        select_sql = "select `domain`,`html` from aizhan2_copy"
        try:
            cursor.execute(select_sql)
            while True:
                row = cursor.fetchone()
                if row:
                    print(row['domain'])
                else:
                    break
            self.conn.commit()
        except Exception as e:
            print('查询错误', e)
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    """
    插入
    """
    def insert(self):
        cursor = self.conn.cursor()

        insert_sql = "insert into `wiwj_sh_ershoufang` (house_title, id)values('%s','%s')" % ("hahahha", "1")

        try:
            select_sql = "select `id` from `wiwj_sh_ershoufang` where id='%s'" % "1"
            response = cursor.execute(select_sql)
            self.conn.commit()
            if response == 1:
                print(u'已存在...')
            else:
                try:
                    cursor.execute(insert_sql)
                    self.conn.commit()
                    print(u'插入成功...')
                except Exception as e:
                    print(u'插入错误...', e)
                    self.conn.rollback()
        except Exception as e:
            print(u'查询错误...', e)
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    """
    更新 预编译防SQL注入
    """
    def update(self):
        cursor = self.conn.cursor()

        args = [1, "qq.com"]
        update_sql = "update `aizhan2_copy` set isparse=%s where domain=%s"
        try:
            # 使用如此参数带入方式，python会自动过滤args中的特殊字符，制止SQL注入的产生
            cursor.execute(update_sql, args)
            self.conn.commit()
        except Exception as e:
            print(u'更新错误...', e)
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    """
    删除
    """
    def delete(self):
        cursor = self.conn.cursor()

        delete_sql = "delete from aizhan2_copy where domain=%s;"
        try:
            # 使用如此参数带入方式，python会自动过滤args中的特殊字符，制止SQL注入的产生
            cursor.execute(delete_sql, "aaa.com")
            self.conn.commit()
        except Exception as e:
            print(u'删除错误...', e)
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()


if __name__ == '__main__':
    pymysqlpython = PymysqlPython()
    pymysqlpython.select()
