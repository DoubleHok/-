# list 的操作测试
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension", t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range", t4.timeit(number=1000), "seconds")


# pop操作测试
x = list(range(2000000))
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero", pop_zero.timeit(number=1000), "seconds")
X = list(range(2000000))
pop_end = Timer("X.pop()", "from __main__ import X")
print("pop_end", pop_end.timeit(number=1000), "seconds")


# append和insert操作测试
y = list(range(3000000))
y_append = Timer("y.append(1)", "from __main__ import y")
print("append_time", y_append.timeit(number=1000), "seconds")
y = list(range(3000000))
y_insert = Timer("y.insert(0, 1)", "from __main__ import y")
print("insert_time", y_insert.timeit(number=1000), "seconds")
