# encoding: utf-8
"""
@version: 3.7
@E-mail: DoubleHok@163.com
@file: 
@time: 2020/4/21 21:44
"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        """添加元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push("helllo")
    stack.push("world")
    stack.push(" !")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.items)


