"""

    单向循环列表
"""


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycLinkList:
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

        # 如果时循环链表则最后节点的next 是指向 head 的, 所以判断下一个节点不等于head 链表就没有到头
        while cur is not None:
            print(cur.elem)
            cur = cur.next

            if cur == self._head:
                break

    def add(self, elem):
        node = Node(elem)

        # 如果头节点为none
        if self.is_empty():
            self._head = node

            node.next = self._head

        else:
            node.next = self._head
            cur = self._head

            while cur.next != self._head:
                cur = cur.next

            # 将最后节点next 指向新加入的node ,形成环
            cur.next = node

            self._head = node

    def append(self, elem):
        node = Node(elem)

        if self.is_empty():
            self._head = node
            node.next = self._head

        else:
            cur = self._head

            while cur.next != self._head:
                cur = cur.next

            cur.next = node

            # 将新加入的尾节点指向头节点, 形成环
            node.next = self._head

    def insert(self, elem, pos):
        if pos <= 0:
            self.add(elem)

        elif pos > (self.length() - 1):
            self.append(elem)

        else:
            node = Node(elem)

            cur = self._head
            count = 0

            # 获取尾节点
            while count < (pos - 1):
                count += 1
                cur = cur.next

            # 将旧尾节点指向的节点交给新尾节点
            node.next = cur.next
            cur.next = node

    def remove(self, elem):
        if self.is_empty():
            return

        cur = self._head
        pre = None

        while cur.next != self._head:
            if cur.elem == elem:

                # 判断是否为头节点
                if cur == self._head:
                    rear = self._head

                    while rear.next != self._head:
                        rear = rear.next

                    self._head = cur.next
                    rear.next = self._head

                else:
                    pre.next = cur.next

                return

            else:
                pre = cur
                cur = cur.next

        if cur.elem == elem:
            if cur == self._head:
                self._head = None

            else:
                pre.next = self._head

    def search(self, elem):
        if self.is_empty():
            return  False

        cur = self._head

        if cur.item == elem:
            return True

        while cur.next != self._head:
            cur = cur.next

            if cur.elem == elem:
                return True

        return False


if __name__ == '__main__':
    ll = SingleCycLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())

    ll.travel()
    print(ll.search(3))

    print(ll.search(7))

    ll.remove(1)
    print("length:", ll.length())

    ll.travel()
