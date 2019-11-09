# 拆出的 .py 文件就是一个模块
# 拆除的目录可能就是一个包

# 引入同级目录下的test模块
import test

print(test.add(10,20))

#sys Python标准库自带的模块。一些和Python解释器相关的
import sys
for line in sys.path:
    print(line)