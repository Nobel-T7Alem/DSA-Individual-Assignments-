# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class definition
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a node at a specific position
    def insertAtPos(self, data, pos):
        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 1

            while current and count < pos - 1:
                current = current.next
                count += 1

            if current is None:
                raise IndexError("Position out of range")

            new_node.next = current.next
            current.next = new_node

    # Method to delete a node at a specific position
    def deleteAtPosition(self, pos):
        if self.head is None:
            raise IndexError("List is empty")

        if pos == 1:
            self.head = self.head.next
        else:
            current = self.head
            count = 1

            while current and count < pos - 1:
                current = current.next
                count += 1

            if current is None or current.next is None:
                raise IndexError("Position out of range")

            current.next = current.next.next

    # Method to delete a node after a specific node
    def deleteAfterNode(self, node):
        if node is None or node.next is None:
            raise ValueError("Invalid node")

        node.next = node.next.next

    # Method to search for a node with a specific value
    def searchNode(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    # Helper method to print the list
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Stack class definition
class Stack:
    def __init__(self):
        self.stack = LinkedList()

    # Method to push a node onto the stack
    def push(self, data):
        self.stack.insertAtPos(data, 1)

    # Method to pop a node from the stack
    def pop(self):
        if self.stack.head is None:
            raise IndexError("Stack is empty")

        data = self.stack.head.data
        self.stack.deleteAtPosition(1)
        return data

    # Method to peek at the top node of the stack
    def peek(self):
        if self.stack.head is None:
            raise IndexError("Stack is empty")

        return self.stack.head.data

# Example usage
if __name__ == "__main__":
    # Testing LinkedList
    linked_list = LinkedList()
    linked_list.insertAtPos(10, 1)
    linked_list.insertAtPos(20, 2)
    linked_list.insertAtPos(30, 3)

    print("After inserting nodes at positions 1, 2, and 3:")
    linked_list.printList()

    linked_list.deleteAtPosition(2)
    print("After deleting node at position 2:")
    linked_list.printList()

    linked_list.deleteAfterNode(linked_list.head)
    print("After deleting node after the head:")
    linked_list.printList()

    print("Searching for node with value 10:", linked_list.searchNode(10))
    print("Searching for node with value 30:", linked_list.searchNode(30))

    # Testing Stack
    stack = Stack()
    stack.push(100)
    stack.push(200)
    stack.push(300)

    print("\nAfter pushing 100, 200, and 300 onto the stack:")
    current = stack.stack.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Peek at the top node of the stack
    print(f"Peek at the top of the stack: {stack.peek()}")

    # Pop nodes from the stack
    print(f"Pop from the stack: {stack.pop()}")

    print("Stack after popping the top element:")
    current = stack.stack.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print(f"Peek at the top of the stack after pop: {stack.peek()}")
