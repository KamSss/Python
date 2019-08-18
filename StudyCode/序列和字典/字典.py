# python的字典是一种映射类型数据。里面的数据是键值对 python是基于hash实现的
a = {
    10:20,
    'key':'value',
    'a':100
}

a = {
    'ip':'127.0.0.1',
    'port':80
}
print(a['ip'])
# 遍历
#for key in a:
#   print(key,value)

# key不能改 只能改value
a['ip'] = '128.0.0.1'
a['id'] = 'hehe' # 修改不存在的对象会被创建
print(a)
# 删除
del(a['ip'])
print(a)