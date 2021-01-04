#!/usr/bin/env python3   #告诉系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*-  #告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print('Hello World')

print('The quick brown fox', 'jumps over', 'the lazy dog')

#feature
# 10_000_000_000 = 10000000000   0xa1b2c3d4 = 0xa1b2_c3d4

# 布尔值可以用and、or和not运算。
print(5 > 3 or 1 > 3)  # true


#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。


#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量
#同一个变量可以反复赋值，而且可以是不同类型的变量
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
a = 123   # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)


#Python解释器干了两件事情
#   1.首先在内存中创建了一个'ABC'的字符串
#   2.然后在内存中创建了一个名为a的变量，并把它指向'ABC'
#   可以尝试把变量a理解为指针
a = 'ABC'   # 指针a指向了一段内存空间ABC
b = a       # 指针b和a指向同一段
a = 'XYZ'   # 创建了新的一段内存空间XYZ，并将指针a重新指向XYZ
print(b)    

#在Python中，通常用全部大写的变量名表示常量
#事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变
#用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
PI = 3.14159265359

#在Python中，有两种除法  /   // 
print(10 / 3) # 3.3333333
print(10 // 3) # 3
print(10 % 3) # 1  取余运算


#ASCII Unicode UTF-8
#https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896
#ASCII编码是1个字节，共128个，够英文用了
#Unicode编码通常是2个字节，能够统一所有语言
#纯Unicode编码有点浪费空间，可以转化为“可变长编码”的UTF-8编码

print('包含中文的str')

print(ord('A'))    #65
print(ord('中'))   #20013
print(chr(66))     #'B'
print(chr(25991))  #'文'

#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。

#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#'ABC'.encode('ascii')
#'中文'.encode('utf-8')

#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes
#b'ABC'.decode('ascii')
#b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
# len('ABC')  #3
# len('中文') #2
# len(b'ABC') #3
# len('中文'.encode('utf-8')) #6
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。


#如何输出格式化的字符串
#在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
#   %d  %f  %s  %x
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#使用以f开头的字符串，称之为f-string，
#r = 2.5
#s = 3.14 * r ** 2
#print(f'The area of a circle with radius {r} is {s:.2f}')


from F1_quadratic import quadratic
from F2_power import power, enroll

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')



