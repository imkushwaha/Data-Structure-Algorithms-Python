# Insertion Method in Singly Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):             # --- Overall Time Complexity: O(n) and Space Complexity: O(1)
        newnode = Node(value)
        if self.head is None:       # ----O(1)
            self.head = newnode     # ----O(1)
            self.tail = newnode     # ----O(1)
        else:
            if location == 0:   # insertion at first  # ----O(1)
                newnode.next = self.head              # ----O(1)
                self.head = newnode                   # ----O(1)

            elif location == -1:  # insertion at last
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode

            else:  # insertion at any given position
                tempNode = self.head
                index = 0
                while index < location -1:            # ----O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newnode
                newnode.next = nextNode


singlyLinkedList = SLinkedList()
# inserting element at first position
singlyLinkedList.insert(1, 0)
# inserting element at last (seq by seq)
singlyLinkedList.insert(2, -1)
singlyLinkedList.insert(3, -1)
singlyLinkedList.insert(4, -1)

# inserting element at first
singlyLinkedList.insert(40, 0)

# inserting element at 3rd position
singlyLinkedList.insert(300, 3)

# print
print([node.value for node in singlyLinkedList])

