import warnings


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

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAt(self, data, pos: int):
        if pos == 0:
            self.insertAtBeginning(data)
            return

        new_node = Node(data)
        curr = self.head

        try:
            for _ in range(pos-1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        except AttributeError:
            warnings.warn('Position passed is out of bounds', RuntimeWarning)

    def deleteFromBeginning(self):
        if self.head == None:
            warnings.warn('Linked List is empty', RuntimeWarning)
            return None

        todel = self.head
        return_val = todel.data
        if todel.next == None:
            self.head = None
        else:
            self.head = todel.next

        del todel
        return return_val

    def deleteFromEnd(self):
        if self.head == None:
            warnings.warn('Linked List is empty', RuntimeWarning)
            return None

        curr = self.head
        if curr.next == None:
            todel = self.head
            self.head = None

        else:
            while curr.next.next:
                curr = curr.next
            todel = curr.next
            curr.next = None

        return_val = todel.data
        del todel
        return return_val

    def deleteFrom(self, pos: int):
        if pos == 0:
            self.deleteFromBeginning()
            return

        curr = self.head

        try:
            for _ in range(pos-1):
                curr = curr.next
            todel = curr.next
            curr.next = curr.next.next
            return_val = todel.data
            del todel
            return return_val
        except AttributeError:
            warnings.warn('Position passed is out of bounds', RuntimeWarning)

    def printList(self, seperator=" -> "):
        if self.head == None:
            warnings.warn('Linked List is empty', RuntimeWarning)
            return

        curr = self.head
        while curr is not None:
            print(curr.data, end=seperator)
            curr = curr.next
        print("\b"*len(seperator) + " "*len(seperator) + "\b"*len(seperator))

    def toList(self):
        if self.head == None:
            warnings.warn('Linked List is empty', RuntimeWarning)
            return

        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __len__(self):
        c = 0
        curr = self.head
        while curr:
            c += 1
            curr = curr.next
        return c

    def __getitem__(self, key):
        if type(key) is not int:
            raise TypeError

        if self.head is None:
            raise IndexError

        if key == 0:
            return self.head.data

        elif key > 0:
            curr = self.head
            try:
                for _ in range(key):
                    curr = curr.next
                return curr.data
            except AttributeError:
                warnings.warn('Index passed is out of bounds', RuntimeWarning)

    def __setitem__(self, key, value):
        if type(key) is not int:
            raise TypeError

        if self.head is None:
            raise IndexError

        if key == 0:
            self.head.data = value

        elif key > 0:
            curr = self.head
            try:
                for _ in range(key):
                    curr = curr.next
                curr.data = value
            except AttributeError:
                warnings.warn('Index passed is out of bounds', RuntimeWarning)

    def __delitem__(self, key):
        self.deleteFrom(key)

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    