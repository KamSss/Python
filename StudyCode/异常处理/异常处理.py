# 我们应该明确知道 try 之中的代码会抛出哪些异常
# 再有针对性的处理
try:
    # 模拟访问越界 并捕获异常
    a = [1,2,3]
    print(a[100])
except IndexError as e:
    print('这是捕获到异常之后的代码:',e)
except NameError as e:
    print('这是 NameError 的异常',e)

#except: 捕获所有异常 不推荐这么写
#Exception是所有异常的父类 可以捕获所有异常 不到万不得已，不要这么写，写这个说明你也不知道要怎么处理异常了
except Exception as e:
    print(e)
# 异常出现之后，会一层一层向上传递，如果每一步都没人处理，最后传到解释器里就会报错

else:
    print('没抛出异常')
    # 如果try中没抛异常，就执行else里面的内容
    # 如果抛出异常了，就不执行else
finally:
    # 无论是否抛异常，无论上面是什么逻辑
    # 下面一定会执行finally
    # 做一些善后工作