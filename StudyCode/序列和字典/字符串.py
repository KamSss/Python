# 大多数的对象都是不可变的 列表和字典是可变对象
# 动态类型的本质是创建一个新对象 把原来的标签指向新对象
a = 'aaaa'
a[0] = 'z'
print(a) # 会报错 因为str类型的a是不可变的 
# 那要怎么变？
a = 'z' + a[1:]
print(a)

# 原始字符串 (正则表达式中很方便)
a = r'hello \n world'

# 字符串切分 合并
a = 'aaa,bb,ccc,ddd'
b = a.split(',')
print(b)
print(',',join(b))

# 判定字符串开头结尾
a = 'hello world'
print(a.startswith('hello'))
print(a.endwith('world'))

# 去除字符串开头结尾的空格/制表符 还有去左空格和去右空格lstrip rstrip
a = ' hello world '
print(a.strip())

# 左对齐 右对齐 居中对齐
a = 'hello world'
print('[' + a.ljust(30) + ']')

# 查找子串
print(a.find('world'))
# 替换子串（不能修改 只能创建新的来替换）
print(a.replace('world','hehe'))