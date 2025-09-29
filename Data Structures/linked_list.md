# Linked Lists  

## Introduction  
A **linked list** is a linear data structure where elements (called **nodes**) are linked together using pointers or references.  
Unlike arrays, linked lists are **dynamic** and can efficiently grow or shrink without reallocating memory.  

---

## Structure of a Linked List  

A singly linked list typically contains:  
- **Head** → the first node in the list  
- **Node(s)** → each containing `data` and a pointer to the `next` node  
- **Tail** → the last node, which points to `None`  

Representation:  

---

## Linked List in Python  

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def stringify_list(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value) + " → "
            current = current.next
        return result + "None"

# Create a linked list
ll = LinkedList()

# Insert elements
ll.insert_beginning(5)
ll.insert_beginning(10)
ll.insert_beginning(15)

# Print the list
print(ll.stringify_list())
```
Key Operations on Linked Lists

Insertion

At the head

At the tail

In the middle

Deletion

Remove head node

Remove tail node

Remove specific value

Traversal

Move through the list from head to tail

Searching

Find if a value exists within the list

Advantages

Dynamic size (no need to predefine capacity)

Efficient insertions and deletions compared to arrays

Disadvantages

Sequential access (no direct indexing)

Extra memory overhead for storing pointers

Key Points to Remember

A linked list is a chain of nodes.

Each node contains data and a pointer to the next node.

The head points to the first node, and the tail points to None.

Useful for dynamic data structures and memory-efficient operations
