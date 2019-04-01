import pymongo


class PymongoPython(object):
    def __init__(self):
        # 这里为了简便，共用一个数据库连接，实际项目中应该对每个操作提供一个连接，或者做一个连接池
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        # self.db = self.client.test
        self.db = self.client['test']
        self.select_list = []

    """
    保存
    """
    def save(self):
        collection = self.db['first']
        # to_save must be an instance of dict, bson.son.SON, bson.raw_bson.RawBSONDocument,
        # or a type that inherits from collections.MutableMapping
        # save: 若新增数据的主键已经存在，则会对当前已经存在的数据进行修改操作。不存在该主键，则插入
        collection.save({'func': 'save'})

    """
    插入
    """
    def insert(self):
        # 若插入的主键已存在则报错：
        # pymongo.errors.DuplicateKeyError:
        # E11000 duplicate key error collection: test.first index: _id_ dup key: { : 1 }
        datas = [
            {'_id': 1, 'data': 12},
            {'_id': 2, 'data': 22},
            {'_id': 3, 'data': 'cc'}
        ]
        datas2 = [
            {'_id': 4, 'data': 'a'},
            {'_id': 5, 'data': 'b'},
            {'_id': 6, 'data': 'c'}
        ]
        collection = self.db['first']
        # 不建议直接使用 insert()
        # collection.insert(datas2)

        # 插入一条
        result_one = collection.insert_one({'_id': 8, 'name': 'joe'})
        print(result_one.inserted_id)

        # 插入多条，数据以列表形式传递
        result_many = collection.insert_many(datas)
        print(result_many.inserted_ids)

        # 查询集合中全部数据
        res = collection.find()
        for r in res:
            print(r)

    """
    更新 one 查询条件为 name=joe 的数据，将其更新为 joel
    """
    def updateone(self):
        collection = self.db.first
        condition = {'name': 'joe'}
        student = collection.find_one(condition)
        student['name'] = 'joel'
        result = collection.update_one(condition, {'$set': student})
        print(result)
        # 匹配的数据条数，影响的数据条数
        print(result.matched_count, result.modified_count)

    """
    更新 many 查询 _id 小于10 的数据，并将每一条符合条件的数据添加 age=1
    """
    def updatemany(self):
        collection = self.db.first
        condition = {'_id': {'$lt': 10}}
        result = collection.update_many(condition, {'$inc': {'age': 1}})
        print(result)
        print(result.matched_count, result.modified_count)

    """
    更新插入 查询 _id 小于10 的数据，并将每一条符合条件的数据的 age + 2
    """
    def up_sert(self):
        collection = self.db.first
        condition = {'_id': {'$lt': 10}}
        result = collection.update_many(condition, {'$inc': {'age': 2}}, upsert=True)
        print(result)
        print(result.matched_count, result.modified_count)

    """
    删除 名字为joel的数据
    """
    def delete(self):
        collection = self.db.first
        result = collection.remove({'name': 'joel'})
        print(result)

    """
    删除 删除名字为joel的，批量删除age小于4的
    """
    def delete_one_many(self):
        collection = self.db.first
        result = collection.delete_one({'name': 'joel'})
        print(result)
        print(result.deleted_count)
        result = collection.delete_many({'age': {'$lt': 4}})
        print(result.deleted_count)

    """
    查询 
    """
    def finds(self):
        collection = self.db.first
        # 查询全部内容
        result = collection.find()
        for r in result:
            print(r)
        # 查询符合条件的一个内容
        result_one = collection.find_one({'func': 'save'})
        print(result_one)


if __name__ == '__main__':
    pymongopython = PymongoPython()
    pymongopython.finds()
