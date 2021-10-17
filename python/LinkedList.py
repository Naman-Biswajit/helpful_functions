from LinkedLists.Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def search(self, value):

        curr = self.head

        if not curr:
            return None

        while curr:
            if curr.value == value:
                return curr
            curr = curr.next

        return None

    def remove(self, value):
        """ Remove first occurrence of value. """
        if not self.head:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return

        curr = self.head.next
        while curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                return
            curr = curr.next

        return None

    def pop(self):
        if not self.head:
            return None
        popped = self.head
        self.head = self.head.next
        return popped.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        if pos == 0:
            self.prepend(value)
            return

        curr = self.head
        count = 0
        while curr.next and count <= pos:
            if count == pos -1:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            count +=1
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        count = 0

        if not self.head:
            return count

        curr = self.head
        while curr:
            count += 1
            curr = curr.next

        return count

    @staticmethod
    def is_circular(linked_list):
        """
        Create 2 pointers one faster than the other, and if the fast one
        reaches the slow one before ending then it must be circular
        :param linked_list:
        :return: bool
        """
        p1 = linked_list.head  # fast
        p2 = linked_list.head  # slow
        while p1 and p1.next:
            p2 = p2.next
            p1 = p1.next.next
            if p1 == p2:
                return True

        return False


def test():
    print("TESTS STARTING")
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)

    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"


    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

    print("TESTS FINISHED")


test()