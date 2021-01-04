#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))




# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def func_multi(x):
    return x * x
# 结果r是一个Iterator，Iterator是惰性序列
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
r = map(func_multi, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)

# map()作为高阶函数，事实上它把运算规则抽象了
# 把这个list所有数字转为字符串
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))   # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做函数计算
from functools import reduce
def add(x, y):
    return x + y

def fn(x, y):
    return x * 10 + y

reduce(add, [1, 3, 5, 7, 9])  # 25
reduce(fn, [1, 3, 5, 7, 9])   #13579

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# 用lambda函数进一步简化成
def char2num(s):
    return DIGITS[s]

def str2int_2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# ['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
   name=name[0].upper()+name[1:].lower()
   return name

list(map(normalize, L1))


# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def tmp_func(x, y):
        return x * y
    return reduce(tmp_func, L)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
'''
1. 找到小数点的位置
2. 将原来的字符串去掉小数点
3. 先通过 map 将 字符 转为 整型
4. 通过 reduce 将字符串转为整数
5. 最后通过小数点的位置乘上 10 -n 次幂
'''
def str2float(s):
    n = 0
    result = []
    for i in range(0, len(s)):
        if s[i] == '.':
            n = i
        else:
            result.append(s[i])
    
    result = list(map(lambda x: int(x), result))
    return reduce(lambda x, y: x * 10 + y, result) * pow(10, n * -1)

