# 序列的内建函数：len max min sorted排序 sum
# enumerate: 同时枚举出序列的下标和值
def Find(input_list, x):
for i, item in enumerate(input_list):
if item == x:
return i
else:
return None
# zip 拉链:也就是矩阵的行列互换！
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
for i in zip(a,b,c):
    print(i)