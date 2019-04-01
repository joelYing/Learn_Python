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


if __name__ == '__main__':
    redispython = RedisPython()
    redispython.string_operation()
