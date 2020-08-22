from LinkedList import SinglyLinkedList, Node

def join(*slls):
    joinedSLL = SinglyLinkedList()
    disconnectedHead = None
    curr = None
    for sll in slls:
        for data in sll:
            new_node = Node(data)
            if curr is None:
                disconnectedHead = new_node
                curr = disconnectedHead
            else:
                curr.next = new_node
                curr = curr.next

    joinedSLL.head = disconnectedHead
    return joinedSLL
        