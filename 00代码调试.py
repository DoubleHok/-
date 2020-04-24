# encoding: utf-8
"""
@version: 3.7
@author: DoubleHok@163.com
@file: 
@time: 2020/4/20 17:07
"""


def sum_demo(x, y):
    for _ in range(2):
        x += 1
        y += 1
        result = x + y
    return result


if __name__ == '__main__':
    result = sum_demo(1, 1)
    print(result)
