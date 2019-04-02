# -*- coding = utf8 -*-

import time
import redis


class RedisPython(object):
    def __init__(self):
        # db=1 选择 redis 中的 db1； 若设置了密码，则需加上 password=
        # self.r = redis.Redis(host='localhost', port=6379, password=12138000, db=1)

        # redis 连接池
        self.pool = redis.ConnectionPool(host='localhost', port=6379, password=12138000, db=1)
        self.r = redis.Redis(connection_pool=self.pool)

    """
    管道
    """
    def pipeline(self):
        pipe = self.r.pipeline(transaction=True)

        self.r.set('name', 'zhangsan')
        self.r.set('name', 'lisi')

        pipe.execute()

    """
    String操作
    """
    def string_operation(self):
        # 保留时长 5秒
        # self.r.set("name", "hehe", ex=5)
        # self.r.get("name")
        # time.sleep(5)
        # self.r.get("name")

        # 存储字典格式 批量设置 mset
        self.r.mset({'k1': 'v1', 'k2': 'v2'})
        self.r.mset(k3='v3', k4='v4', k5='v5')

        # 批量获取
        print(self.r.mget(['k1', 'k3']))

        # 打印原值, 设置新值
        print(self.r.get('k5'))
        print(self.r.getset('k5', '5v'))
        print(self.r.get('k5'))

        # 获取子序列（根据字节获取）
        self.r.set('writer', '徐凤年')
        # 开头的b表示这是一个bytes类型。\xe4是十六进制的表示方式，它占用1个字节的长度
        # 因此”中文“被编码成utf-8后，我们可以数得出一共用了6个字节，每个汉字占用3个
        # 这印证了上面的论述。在使用内置函数bytes()的时候，必须明确encoding的参数，不可省略
        print(str(self.r.getrange('writer', 0, 5), encoding='utf-8'))

        # 修改字符串内容，从指定字符串索引开始向后替换
        self.r.set('reader', 'ok')
        self.r.setrange('reader', 1, 'ko')
        print(self.r.get('reader'))

        # 追加字符
        self.r.append('reader', 'k')
        print(self.r.get('reader'))

    """
    Hash
    """
    def hash_operation(self):
        # 存储字典格式 批量设置 hmset
        self.r.hmset('h1', {'k7': 'v7', 'k8': 'v8'})

        # 批量获取
        print(self.r.hmget('h1', ['k7', 'k8']))

        # 获取hash对应的所有键值
        print(self.r.hgetall('h1'))

        print(self.r.hkeys('h1'))
        print(self.r.hvals('h1'))

        # 检查对应的key是否存在
        print(self.r.hexists('h1', 'k7'))

        # 增量式迭代获取，分片获取数据, 用于数据量大的时候
        print(self.r.hscan('h1'))

    """
    List
    """
    def list_operation(self):
        # 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
        self.r.lpush('1', [11, 12, 13])
        self.r.lpush('1', [14, 15, 16])
        # 偏移start和stop是基于零的索引
        print(self.r.lrange('1', 1, 1))
        # ?
        print(self.r.lrange('1', 1, 2))

        # 在name对应的列表的某一个值前或后插入一个新值
        self.r.lpush("2", "AA", "BB", "CC", "DD")
        print(self.r.lrange("2", 0, 2))
        self.r.linsert('2', 'Before', 'CC', 'cc')
        print(self.r.lrange("2", 0, 3))

        # 使用 自定义redis列表增量迭代
        for item in self.list_iter('2'):
            print(item)

    def list_iter(self, name):
        list_count = self.r.llen(name)
        for index in range(list_count):
            yield self.r.lindex(name, index)

    """
    Set Set集合就是不允许重复的列表
    """
    def set_operation(self):
        self.r.sadd('3', 'aa')
        self.r.sadd('3', 'aa', 'bb')
        # 获取对应集合的所有成员
        print(self.r.smembers('3'))
        # 获取集合中对应的元素个数
        print(self.r.scard('3'))
        


if __name__ == '__main__':
    redispython = RedisPython()
    redispython.set_operation()
