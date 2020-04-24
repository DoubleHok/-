# 节点实现
class SingleNode(object):
    """单链表的节点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


# 单链表的实现
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is__empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur 初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾节点时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print(" ")

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = SingleNode(item)
        # 先判断链表是否为空，若为空链表，则将_head指向新节点
        if self.is__empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        """头部添加新节点"""
        # 先创建一个保存item值得节点
        node = SingleNode(item)
        # 将新节点的链接区域指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 插入位置在第一个元素之前，执行头部插入
        if pos <= 0:
            self.add(item)
        # 插入位置超过链表尾部，则执行尾部插入
        if pos >= (self.length()):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre :
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将深处位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并放回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


# 测试
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.travel()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
