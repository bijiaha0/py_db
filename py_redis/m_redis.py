import redis
import time

# 普通连接
r = redis.StrictRedis(host='localhost',port=6378,db=0)

print(r)
