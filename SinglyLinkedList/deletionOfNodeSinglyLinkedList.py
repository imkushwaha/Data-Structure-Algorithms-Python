
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

    # Insertion Singly Linked List
    def insert(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:  # insertion at first
                newnode.next = self.head
                self.head = newnode

            elif location == -1:  # insertion at last
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode

            else:  # insertion at any given position
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newnode
                newnode.next = nextNode

    # Traversal Singly Linked List
    def traversal(self):  # Overall Time Complexity of Traversal method is O(n) and Space Complexity O(1)

        if self.head is None:  # ------- O(1)
            print("The Singly Linked List does not exist")  # ------ O(1)
        else:
            node = self.head  # ------- O(1)
            while node is not None:
                print(node.value)  # -------- O(n)
                node = node.next  # -------- O(1)

    # Search for a node in Singly Linked List
    def search(self, nodevalue):         # Time Complexity : O(n) and Space Complexity : O(1)

        if self.head is None:     # ------- O(1)
            return "The list does not exist"
        else:
            node = self.head      # ------- O(1)
            while node is not None:  # ---- O(n)
                if node.value == nodevalue:
                    return node.value   # ---- O(n)
                node = node.next
            return "The value does not exist in this list"

    # Delete a node from Singly Linked List
    def deletenode(self, location):            # Time Complexity: O(n) and Space complexity: O(1)
        if self.head is None:                  # ------ O(1)
            print("The SLL does not exist")
        else:
            if location == 0:   # delete first node   # ------ O(1)
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            elif location == 1:     # delete last node
                if self.head == self.tail:
                    self.head = None     # ------ O(1)
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:    # ------ O(n)
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node    # ------ O(1)

            else:
                tempnode = self.head
                index = 0
                while index < location - 1:    # ------ O(n)
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next


singlyLinkedList = SLinkedList()
singlyLinkedList.insert(1, -1)
singlyLinkedList.insert(2, -1)
singlyLinkedList.insert(3, -1)
singlyLinkedList.insert(4, -1)
singlyLinkedList.insert(5, -1)
singlyLinkedList.insert(6, -1)
singlyLinkedList.insert(40, 2)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deletenode(1)
print([node.value for node in singlyLinkedList])
