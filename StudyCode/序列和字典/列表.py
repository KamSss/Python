# 因为列表可以插入删除 所以可以当作栈、队列来使用
# 删除 
a = [1,2,3,4]
del(a[3])
print(a)
a.pop(-1)
print(a)

# 队列
a.append(50)
a.pop(0)
print(a)

# 返回一个对象出现次数
print(a.count(1))

# 列表的深浅拷贝
import copy
a = [1,2,3,4]
# 深拷贝只能针对可变对象使用
b = copy.deepcopy(a)
a[0] = 100
print(b)