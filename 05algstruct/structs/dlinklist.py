"""
    双向链表
"""


class Node:
    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next
        self.pre = None


class DLinkList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        cur = self._head

        while cur is not None:
            print(cur.elem, end='\t')
            cur = cur.next

        print()

    def add(self, elem):
        node = Node(elem)

        if self.is_empty():
            self._head = node

        else:
            # node next 指向head 结点
            node.next = self._head
            self._head.pre = node
            self._head = node

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            self._head = node

        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next

            # 节点处理
            cur.next = node
            node.pre = cur

    def search(self, elem):
        cur = self._head
        while cur is not None:
            if cur.elem == elem:
                return True

            cur = cur.next

        return False

    def insert(self, elem, pos):
        if pos <= 0:
            self.add(elem)

        elif pos > (self.length() - 1):
            self.append(elem)

        else:
            node = Node(elem)

            cur = self._head
            count = 0

            while count < (pos - 1):
                count += 1
                cur = cur.next

            node.pre = cur
            node.next = cur.next
            cur.next.pre = node
            cur.next = node

    def remove(self, elem):
        cur = self._head

        while cur is not None:
            if cur.elem == elem:
                # 判断是否为头节点

                if cur == self._head:
                    # 将头节点指向下一个节点
                    self._head = cur.next

                    # 如果下一个节点不为None, 需要将下一个节点的pre 置为None, 而不是之前头节点的值
                    if cur.next:
                        cur.next.pre = None

                else:
                    # 不是头节点
                    # 将下一个节点的上一级节点指向
                    cur.pre.next = cur.next

                    if cur.next:
                        cur.next.pre = cur.pre

                break

            else:
                cur = cur.next


if __name__ == '__main__':
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print(ll.length())
    ll.travel()

    print(ll.search(3))
    print(ll.search(5))
    ll.remove(3)
    print(ll.length())
    ll.travel()
