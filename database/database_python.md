## MYSQL
### pymysql SSDictCursor 流式字典游标

如果用传统的 fetchall() 或 fetchone() 方法，都是先默认在内存里缓存下所有行然后再处理，大量的数据会导致内存资源消耗光，内存容易溢出。
流式游标 避免客户端占用大量内存。(这个 cursor 实际上没有缓存下来任何数据，它不会读取所有所有到内存中，它的做法是从储存块中读取记录，并且一条一条返回给你。)

使用迭代器而不用 fetchall ,即省内存又能很快拿到数据

注意：
因为 SSCursor 是没有缓存的游标,结果集只要没取完，这个 conn 是不能再处理别的 sql，包括另外生成一个 cursor 也不行的。如果需要干别的，请另外再生成一个连接对象。
每次读取后处理数据要快，不能超过 60 s，否则 mysql 将会断开这次连接，也可以修改 SET NET_WRITE_TIMEOUT = xx 来增加超时间隔。

### execute 防SQL注入
execute() 函数本身有接受sql语句参数位的，可以通过python自身的函数处理sql注入问题。
```
args = (id, type)
cur.execute('select a, b, c from x where b = %s and c = %s', args)
```
使用如此参数带入方式，python会自动过滤args中的特殊字符，制止SQL注入的产生。

execute()函数本身就有接受SQL语句变量的参数位，只要正确的使用（直白一点就是：使用”逗号”，而不是”百分号”）就可以对传入的值进行correctly转义，从而避免SQL注入的发生。

## MongoDB
### save()
如果能根据_id找到一个已经存在的文档，那么就更新。如果没有传入_id参数或者找不到存在的文档，那么就插入一个新文档。

MongoDB 要求每个文档都必须有 _id 
如果待插入的文档没有 _id, MongoDB 会自动生成一个,但不会把结果返回个 PyMongo
对于需要写操作频繁的应用来说, 在写入之前复制一份插入 _id 代价可能会很高
![id]()

### upsert()
MongoDB 的update 方法的三个参数是upsert，这个参数是个布尔类型，默认是false。
当它为true的时候，update方法会首先查找与第一个参数匹配的记录，在用第二个参数更新之
如果找不到与第一个参数匹配的的记录，就插入一条（upsert 的名字也很有趣是个混合体：update+insert）


| 符号 | 含义 | 示例 |
|:----|:----|:-----------|
|$lt	|小于	|{'age': {'$lt': 20}}
|$gt	|大于	|{'age': {'$gt': 20}}
|$lte	|小于等于	|{'age': {'$lte': 20}}
|$gte	|大于等于	|{'age': {'$gte': 20}}
|$ne	|不等于	|{'age': {'$ne': 20}}
|$in	|在范围内	|{'age': {'$in': [20, 23]}}
|$nin	|不在范围内	|{'age': {'$nin': [20, 23]}}

## Redis
### pipeline
redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作
如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。