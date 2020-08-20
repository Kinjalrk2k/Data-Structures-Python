import unittest
import random
from LinkedList import SinglyLinkedList

RANDMAX = 100
'''
ATTRIBUTES:-
self.test_list -> A python list which contains the elements in order
self.test_SinglyLinkedList -> The actual Singly Linked List Object to do operations
test_insert -> A random test element to insert in the List
test_insert_pos -> A random position to insert the test element at

APPROACH:-
Similar operation is done in both the self.test_list and self.test_SinglyLinkedList
Then they are asserted to equal.
At certain test-cases, warnings are tested: The test case pases when the warning is correctly raised
'''

class TestInsert(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestInsert, self).__init__(*args, **kwargs)

        self.test_list = []
        self.test_SinglyLinkedList = SinglyLinkedList()
        # self.test_list = random.sample(range(0, RANDMAX), 7)    # TODO: change this randomizing parameters

    def test_InsertAtBeginning_once(self):
        test_insert = random.randint(0, RANDMAX)

        self.test_list.insert(0, test_insert)
        self.test_SinglyLinkedList.insertAtBeginning(test_insert)

        self.assertEqual(
            list(self.test_SinglyLinkedList.toList()), self.test_list)

    def test_InsertAtBeginning_multiple(self):
        for _ in range(random.randint(0, RANDMAX//2)):
            test_insert = random.randint(0, RANDMAX)

            self.test_list.insert(0, test_insert)
            self.test_SinglyLinkedList.insertAtBeginning(test_insert)

            self.assertEqual(
                list(self.test_SinglyLinkedList.toList()), self.test_list)

    def test_insertAtEnd_once(self):
        test_insert = random.randint(0, RANDMAX)

        self.test_list.append(test_insert)
        self.test_SinglyLinkedList.insertAtEnd(test_insert)

        self.assertEqual(
            list(self.test_SinglyLinkedList.toList()), self.test_list)

    def test_insertAtEnd_multiple(self):
        for _ in range(random.randint(0, RANDMAX//2)):
            test_insert = random.randint(0, RANDMAX)

            self.test_list.append(test_insert)
            self.test_SinglyLinkedList.insertAtEnd(test_insert)

            self.assertEqual(
                list(self.test_SinglyLinkedList.toList()), self.test_list)

    def test_insertAt0_once(self):
        test_insert = random.randint(0, RANDMAX)

        self.test_list.append(test_insert)
        self.test_SinglyLinkedList.insertAt(test_insert, 0)

        self.assertEqual(
            list(self.test_SinglyLinkedList.toList()), self.test_list)

    def test_insertAt_warning(self):
        test_insert = random.randint(0, RANDMAX)
        test_insert_pos = random.randint(1, RANDMAX)

        with self.assertWarns(RuntimeWarning):
            self.test_SinglyLinkedList.insertAt(test_insert, test_insert_pos)

    def test_insertAt_random(self):
        for i in range(random.randint(0, RANDMAX//2)):
            test_insert = random.randint(0, RANDMAX)
            test_insert_pos = random.randint(0, i)

            self.test_list.insert(test_insert_pos, test_insert)
            self.test_SinglyLinkedList.insertAt(test_insert, test_insert_pos)

            self.assertEqual(
                list(self.test_SinglyLinkedList.toList()), self.test_list)


class TestDelete(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestInsert, self).__init__(*args, **kwargs)

        self.test_list = random.sample(range(0, RANDMAX), RANDMAX//2)
        self.test_SinglyLinkedList = SinglyLinkedList()
        for i in self.test_list:
            self.test_SinglyLinkedList.insertAtEnd(i)


if __name__ == '__main__':
    unittest.main()
