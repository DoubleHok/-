# encoding: utf-8
"""
@version: 3.7
@E-mail: DoubleHok@163.com
@file: 
@time: 2020/4/22 8:17
"""


class Deque(object):
    """双端队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def add_front(self, item):
        """在队头添加元素"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.items.append(item)

    def remove_front(self):
        """在队头删除元素"""
        return self.items.pop(0)

    def remove_rear(self):
        """在队尾删除元素"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)


# 测试
if __name__ == "__main__":
    deq = Deque()
    deq.add_front("hello world")
    deq.add_front("!")
    deq.add_rear("!!")
    print(deq.items)
    print(deq.is_empty())
    print(deq.size())
    deq.remove_front()
    print(deq.items)
    deq.remove_rear()
    print(deq.items)



