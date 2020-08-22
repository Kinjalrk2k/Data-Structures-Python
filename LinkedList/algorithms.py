from LinkedList import SinglyLinkedList, Node
import warnings

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
        
def split(sll, pos):
    leftPart = SinglyLinkedList()
    rightPart = SinglyLinkedList()

    disconnectedHead1 = sll.head
    disconnectedHead2 = None

    curr = sll.head
    try:
        for _ in range(pos-1):
            curr = curr.next
        disconnectedHead2 = curr.next
        curr.next = None
    except AttributeError:
        warnings.warn('Position passed is out of bounds', RuntimeWarning)

    leftPart.head = disconnectedHead1
    rightPart.head = disconnectedHead2

    return(leftPart, rightPart)
