### pymysql SSDictCursor 流式字典游标

如果用传统的 fetchall() 或 fetchone() 方法，都是先默认在内存里缓存下所有行然后再处理，大量的数据会导致内存资源消耗光，内存容易溢出。
流式游标 避免客户端占用大量内存。(这个 cursor 实际上没有缓存下来任何数据，它不会读取所有所有到内存中，它的做法是从储存块中读取记录，并且一条一条返回给你。)

使用迭代器而不用 fetchall ,即省内存又能很快拿到数据

注意：
因为 SSCursor 是没有缓存的游标,结果集只要没取完，这个 conn 是不能再处理别的 sql，包括另外生成一个 cursor 也不行的。如果需要干别的，请另外再生成一个连接对象。
每次读取后处理数据要快，不能超过 60 s，否则 mysql 将会断开这次连接，也可以修改 SET NET_WRITE_TIMEOUT = xx 来增加超时间隔。

### 
execute() 函数本身有接受sql语句参数位的，可以通过python自身的函数处理sql注入问题。
```
args = (id, type)
cur.execute('select a, b, c from x where b = %s and c = %s', args)
```
使用如此参数带入方式，python会自动过滤args中的特殊字符，制止SQL注入的产生。

execute()函数本身就有接受SQL语句变量的参数位，只要正确的使用（直白一点就是：使用”逗号”，而不是”百分号”）就可以对传入的值进行correctly转义，从而避免SQL注入的发生。