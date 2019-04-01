### save()
MongoDB 要求每个文档都必须有 _id 
如果待插入的文档没有 _id, MongoDB 会自动生成一个,但不会把结果返回个 PyMongo
对于需要写操作频繁的应用来说, 在写入之前复制一份插入 _id 代价可能会很高
![id](D:\mygit\learn_python\Learn_Python\static\2019-04-01_132507.png)

