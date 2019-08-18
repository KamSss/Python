def add(x,y):
    return x + y

print(add(10,20))
print(add("hello ","python"))
print(add([1,2,3],[4,5,6]))

#传一个参数就覆盖第一个默认值
def add2(x=0,y=0):
    return x + y
print(add2(10))

def add3(x=0,y=0,z=0):
    print(x,y,z)
    return x + y
print(add3(10,10))
# 有没有办法 让x=10 y默认值 z=10? C++做不到
print(add3(x=10,z=10))

#默认参数
print(10,20,30,40,sep',',end';')