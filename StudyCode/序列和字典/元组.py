def get_point():
    return 10,20
a = get_point()
print(type(a))

# 元组的两个重要应用场景：
#   1.函数传参的时候使用元组可以避免函数内部把函数外部的内容修改掉
#   2.元组是可 hash 的，元组就可以作为字典的 key，列表不行
