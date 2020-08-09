from SinglyLinkedList import *

# driver program
if __name__ == "__main__":
    a = SinglyLinkedList()

    for i in range(5):
        a.insertAtBegining(i)

    a.printList()

    for _ in range(5):
        a.deleteFromBeginning()

    a.printList()
    a.deleteFromBeginning()
