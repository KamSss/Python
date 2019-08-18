# 单引号、双引号、三引号括起来都是字符串，这样的写法可以轻松输出含有单引号、双引号、三引号的字符串不需要转义，但是同时也支持转义的语法。
# 比如下列两个字符串写法都可以:
a = 'my name is "white".'
b = "my name is 'white'."
print(a)
print(b)

# 字符串拼接
name = 'zhanghaozheng'
str = ' is cooool'
print(name + str)

# 字符串相乘
print(name * 3)

# 字符串访问 负数表示从倒数第一个开始 
print(name[1])
print(name[-1])
