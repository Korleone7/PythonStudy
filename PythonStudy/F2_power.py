#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 必选参数在前，默认参数在后
# 默认参数必须指向不变对象！！！
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L