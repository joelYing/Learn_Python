from database.RedisHelper.redishelper import RedisHelper

"""
令订阅者保持监听，当执行发布者时，订阅者就能接收到数据
"""
if __name__ == '__main__':
    # 订阅者
    obj = RedisHelper()
    redis_sub = obj.subscribe()

    while True:
        msg = redis_sub.parse_response()
        print(msg)
