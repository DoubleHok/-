# encoding: utf-8
"""
@version: 3.7
@E-mail: DoubleHok@163.com
@file: 
@time: 2020/4/22 7:58
"""


class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def enqueue(self, item):
        """往队列插入元素"""
        self.items.insert(0, item)

    def dequeue(self):
        """删除队列中元素"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)


# 测试
if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue(" !")
    print(q.is_empty())
    print(q.size())
    print(q.dequeue())
    print(q.items)
    print(q.dequeue())
    print(q.items)



