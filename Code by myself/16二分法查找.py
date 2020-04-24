# encoding: utf-8
"""
@version: 3.7
@E-mail: DoubleHok@163.com
@file: 
@time: 2020/4/23 12:17
"""


# 递归实现1
def binary_search1(alist, item):
    n = len(alist)
    if n > 0:
        midpoint = n // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return binary_search1(alist[:midpoint], item)
        elif item > alist[midpoint]:
            return binary_search1(alist[midpoint + 1:], item)
    return False


# 递归实现2
def binary_search2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search2(alist[:midpoint], item)
            else:
                return binary_search2(alist[midpoint + 1:], item)


# 非递归实现
def binary_search3(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid_point = (first+last)//2
        if item == alist[mid_point]:
            return True
        else:
            if item < alist[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False


# 测试
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search3(testlist, 3))
print(binary_search3(testlist, 13))
