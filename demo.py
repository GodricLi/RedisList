# _*_ coding=utf-8 _*_


import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379,
                            max_connections=100)
coon = redis.Redis(connection_pool=POOL)

# 列表操作
"""
    redis = [1,2,3,4,5,66,888,8887,]
        -左右操作
        -阻塞
        
"""
# 1.从左边添加值
coon.lpush('list', 22)
# 2.从右边添加值
coon.rpush('list', 'right')
# 3.从左边获取值
val_left = coon.lpop('list')
# 4.从右边获取值
val_right = coon.rpop('list')
# 5.获取指定范围的数据
data = coon.lrange('list', 0, 10)
# 6.# 阻塞，若取不到值就会阻塞。超时返回None
res = coon.blpop('list', timeout=10)
# res = coon.brpop('list', timeout=10)


# 取出reids中的100w条数据：
"""
    制作一个生成器一点一点的获取数据    
"""


def list_iter(key, count=100):
    """

    :param key:数据库名字
    :param count:每次取出的数据量
    :return:
    """
    index = 0
    while True:
        data_list = coon.lrange(key, index, index + count - 1)
        if not data_list:
            return
        for i in data:
            yield i


for item in list_iter('list1', 5):
    print(item)
