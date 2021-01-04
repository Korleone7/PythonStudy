#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 一元二次方程
def quadratic(a, b, c):
    # pass # pass可以用来作为占位符
    # 参数检查：只允许整数和浮点数类型的参数
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if a == 0:
        raise TypeError('bad operand type')

    delta = b * b - 4 * a * c
    if  delta < 0:
         raise TypeError('delta < 0')

    x1 = (-b + math.sqrt(delta)) / 2 / a
    x2 = (-b - math.sqrt(delta)) / 2 / a
    return x1, x2