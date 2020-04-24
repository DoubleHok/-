# encoding: utf-8
"""
@version: 3.7
@E-mail: DoubleHok@163.com
@file: 
@time: 2020/4/23 16:16
"""


# 先序遍历
def preorder(self, root):
    """递归实现先序遍历"""
    if root is None:
        return
    print(root.elem)
    self.preorder(root.lchild)
    self.preorder(root.rchild)


# 中序遍历
def inorder(self, root):
    """递归实现后续遍历"""
    if root is None:
        return
    self.inorder(root.lchild)
    print(root.elem)
    self.inorder(root.rchild)


# 后序遍历
def postorder(self, root):
    """递归实现后续遍历"""
    if root is None:
        return
    self.postorder(root.lchild)
    self.postorder(root.rchild)
    print(root.elem)


# 层次遍历
def breath_travel(self, root):
    """利用队列实现树的层次遍历"""
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            queue.append(node.lchild)
        if node.rchild is not None:
            queue.append(node.rchild)

