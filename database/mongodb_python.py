import pymongo


class PymongoPython(object):
    def __init__(self):
        # 这里为了简便，共用一个数据库连接，实际项目中应该对每个操作提供一个连接，或者做一个连接池
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        # self.db = self.client.test
        self.db = self.client['test']
        self.select_list = []

    """
    查询
    """
    def select(self):
        datas = [
            {'_id': 1, 'data': 12},
            {'_id': 2, 'data': 22},
            {'_id': 3, 'data': 'cc'}
        ]
        # collection = self.db.first 若没有该集合，则会自动新建一个
        collection = self.db['first']
        collection.insert(datas)
        # 查询集合中全部数据
        res = collection.find()
        for r in res:
            print(r)

    """
    流式游标查询
    """
    def select_ssdictcursor(self):
        pass

    """
    插入
    """
    def insert(self):
        pass

    """
    更新 预编译防SQL注入
    """
    def update(self):
        pass

    """
    删除
    """
    def delete(self):
        pass


if __name__ == '__main__':
    pymongopython = PymongoPython()
    pymongopython.select()
