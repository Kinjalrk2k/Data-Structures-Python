from SinglyLinkedList import *

# driver program
if __name__ == "__main__":
    a = SinglyLinkedList()

    for i in range(5):
        a.insertAtBegining(i)

    a.insertAt(10, 5)
    a.printList()
