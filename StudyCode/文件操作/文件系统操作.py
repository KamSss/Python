import os.path as path

p = '/aaa/bbb/cc.txt'
result = path.split(p)
print(f'[{result}]')
result = path.splitext(p) # 按扩展名分类

#exists 指定路径是否存在
#islink 指定路径是否是一个符号链接

import os
p = 'd:/test'
for item in os.walk(p):
    print(item)

# 删除文件
p = 'd:/test/'
os.remove(p + 'a/1.txt')
# 删除空目录
os.removedirs(p + 'a')
# 删除不为空的目录：rmtree 