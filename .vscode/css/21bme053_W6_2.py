class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        t = self.head
        if t is None:
            print("This List is empty")
        else:
            while t:
                if t.data == data:
                    t = t.next
                else:
                    print(t.data)
                    t = t.next

    def remove_duplicate(self):
        l = []
        temp = self.head
        while temp is not None:
            if temp.data not in l:
                l.append(temp.data)
            temp = temp.next
        print(l)

    def count(self):
        ct = 0
        temp = self.head
        while temp is not None:
            ct += 1
            temp = temp.next
        print(ct)

    def printList(self):
        t = self.head
        if t is None:
            print("List is empty")
        else:
            while t:
                print(t.data)
                t = t.next


dll = DoublyLinkedList()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.insert(6)
dll.insert(7)
dll.insert(8)
dll.insert(8)
dll.printList()
print()
dll.delete(dll.head.next)
dll.printList()
dll.count()
dll.remove_duplicate()