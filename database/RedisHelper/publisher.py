from database.RedisHelper.redishelper import RedisHelper

# 发布者
obj = RedisHelper()
obj.publish('hello')