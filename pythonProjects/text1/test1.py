# coding=utf-8
print 45678 + 0x12fd2

print "Learn Python in imooc"

print 100 < 99

print 0xff == 255


print "hello, python"

print "hello,", "python"

#print "hello, " + "python"

#this is a note!!!

a = "abc"
b = a
a = "xyz"
print b
print a

print r'\(~_~)/\(~_~)/'

# List列表，有序，表内元素可更换(动态,存储的类型可不同)
L = ['A', 'B', "C", "D"]

# 在列表末尾添加元素
L.append("E")

# 在列表指定索引处添加元素
L.insert(2, 'F')

# 从列表指定索引处删除元素
L.pop(3)

# 替换列表中的指定元素
L[2] = 'G'

print L

# tuple列表(元组)，有序，表内元素一旦一定，不可更换(静态)
t = ('Q', 'W', "E", "R", "T")

print t[2]

# 创建单元素tuple时,注意在末尾多加一个逗号',',避免歧义
t = (1,)

print t

# 当tuple列表中含有List列表时,tuple变为'可变'
t = ('a', 'b', ['A', 'B'])

t[2][0] = 'B'
t[2].pop(1)
t[2].append('C')

print t





