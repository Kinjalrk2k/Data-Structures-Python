class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def insertAtBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self, seperator=" -> "):
        curr = self.head
        while curr is not None:
            print(curr.data, end=seperator)
            curr = curr.next
        print("\b"*len(seperator) + " "*len(seperator) + "\b"*len(seperator))



