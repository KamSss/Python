# 读文件
# 所有的返回点都要设置close 避免文件资源泄露 但是这种方法很笨！
def func():
    f = open('d:/test.txt','r')
    x = 10
    if x==10:
        f.close()
        return

#执行文件操作。。。
f.close()

# 上面的方法很容易就忘记close 
# 上下文管理器：
def func():
    with open('d:/test.txt','r') as f:
        # 文件基本操作
        pass
# 遇到乱码 需要encoding = 'utf-8'编码方式统一一下
# open('d:/test.txt','r',encoding = 'utf-8')

# 写文件
#with write