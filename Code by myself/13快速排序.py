# encoding: utf-8
"""
@version: 3.7
@E-mail: DoubleHok@163.com
@file: 
@time: 2020/4/22 10:54
"""


def quick_sort(alist, start, end):
    """快速排序"""
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    midpoint = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准小，则high向左移
        while low < high and alist[high] >= midpoint:
            high -= 1
        # 将high指向的元素放到low位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素不比基准大，则low向右移
        while low < high and alist[low] < midpoint:
            low += 1
        # 将low指向的元素放到high位置上
        alist[high] = alist[low]
    # 对基准元素左边的子序列进行快排序
    quick_sort(alist, start, low - 1)
    # 对基准元素右边的子序列进行快排序
    quick_sort(alist, low + 1, end)


# 测试
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
