# 节点
class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def is_empty(self):
        return self.next is None

    def length(self):
        index = 0
        node = self.next
        while node is not None:
            index += 1
            node = node.next
        return index

    def find(self, val):
        node = self.next
        while node is not None:
            if node.val == val:
                break
            node = node.next
        return node

    def _node_at_index(self, index):
        i = 0
        node = self
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def element_at_index(self, index):
        node = self._node_at_index(index)
        return node.element

    def append(self, node):
        n = self
        while n.next is not None:
            # 确保n是最后一个元素
            n = n.next
        n.next = node
        return

    def prepend(self, node):
        # 找到head 把node赋给head.next
        pass

    # 打印链表： "head > node1 > node2 ..."
    def show(self):
        node = self
        s = ''
        while node is not None:
            if node.next is None:
                s += str(node.val)
            else:
                s += str(node.val) + ' > '
            node = node.next
        print(s)


def test():
    head = Node('head')
    n1 = Node('111')
    n2 = Node('222')
    n1.next = n2
    head.next = n1
    head.show()
    # head > 111 > 222

    n3 = Node('333')
    head.append(n3)
    head.show()
    # head > 111 > 222 > 333


if __name__ == '__main__':
    # test()
    pass