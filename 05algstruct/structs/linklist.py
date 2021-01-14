"""
    自定义链表

"""


# link list node
class Node:
    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next


class SingleLinkList:

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
        """
        头部添加
        :param elem:
        :return:
        """
        node = Node(elem)
        node.next = self._head
        self._head = node

    def append(self, elem):
        """
        尾添加
        :param elem:
        :return:
        """
        node = Node(elem)
        if self.is_empty():
            self._head = node

        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next

            cur.next = node

    def insert(self, elem, pos):
        """
        指定位置添加
        :param elem:
        :param pos:
        :return:
        """

        # pos < 0 时
        if pos <= 0:
            self.add(elem)

        # pos > max length 时
        elif pos > (self.length() - 1):
            self.append(elem)

        # 插入指定位置
        else:
            node = Node(elem)
            count = 0
            pre = self._head

            while count < (pos - 1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        cur = self._head
        pre = None

        while cur is not None:
            # 找到了指定元素
            if cur.elem == elem:
                # 如果第一个元素就是指定的节点

                if not pre:
                    self._head = cur.next

                else:
                    pre.next = cur.next

                break

            else:
                # 后移节点
                pre = cur
                cur = cur.next

    def search(self, elem):
        cur = self._head
        while cur is not None:
            if cur.elem == elem:
                return True

            cur = cur.next

        return False


if __name__ == '__main__':
    # test
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.insert(4, 2)
    ll.travel()

    print(ll.search(4))
    ll.remove(1)
    ll.travel()