# -*- coding: utf-8 -*-

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


#https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

