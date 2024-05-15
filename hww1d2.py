import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

#------------------------------------------------------------#
line_break()
print("Implementing a Singly Linked List in Python")
line_break()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, remove_value):
        if self.head is None:
            return
        if self.head.value == remove_value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == remove_value:
                current.next = current.next.next
                return
            current = current.next
        print(f"{remove_value} is not in this Linked List.")

    def traverse(self):
        current = self.head
        while current:
            print(current, end=' -> ')
            current = current.next
        print(None)

months = SinglyLinkedList()
months.append('Codember')
months.append('January')
months.delete('March')

months.traverse()

#------------------------------------------------------------#
line_break()
print("Implementing a Doubly Linked List in Python")
line_break()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def delete(self, remove_value):
        if self.head is None:
            return
        if self.head.value == remove_value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.value == remove_value:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        print(f"{remove_value} is not in this Linked List.")

    def traverse(self):
        current = self.head
        while current:
            print(current, end=' <--> ')
            current = current.next
        print(None)

days = DoublyLinkedList()
days.append('Thursday')
days.append('Saturday')
days.delete('Sunday')
days.delete('Wednesday')

days.traverse()

