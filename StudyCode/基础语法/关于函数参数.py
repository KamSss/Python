# 关键字参数
# 当我们有多个默认参数，只想传其中几个参数的时候，还可以使用关键字参数的方式进行传参
a = (9,5,2,7)
print(sorted(a)) # sorted内建排序函数 底层算法:TimSort 改进版本的归并排序
# 不管传列表元组 sorted都返回元组 如果你想要列表可以用工厂函数转换
print(a)

# 参数字典
#def log(**msg): msg变成了一个字典