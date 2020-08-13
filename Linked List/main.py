from SinglyLinkedList import *

# driver program
if __name__ == "__main__":
    a = SinglyLinkedList()

    for i in range(5):
        a.insertAtBegining(i)

    # a.insertAt(10, 3)
    a.printList()

    # for _ in range(5):
    #     a.deleteFromEnd()

    a.deleteFrom(5)
    a.printList()
