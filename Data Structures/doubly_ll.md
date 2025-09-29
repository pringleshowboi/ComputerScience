# Doubly Linked Lists  

## Introduction  
A **doubly linked list (DLL)** is a linear data structure where each node contains pointers to both its **previous** and **next** nodes.  
This allows traversal in **both directions** (forward and backward), unlike a singly linked list which can only move forward.  

---

## Structure of a Doubly Linked List  

Each node contains:  
- **Data** → the stored value  
- **Next** → pointer to the next node  
- **Prev** → pointer to the previous node  

Representation:  

---

## Node Representation in Python  

```python
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = DoublyNode(value)
        if self.head is None:  # Empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_tail(self, value):
        new_node = DoublyNode(value)
        if self.tail is None:  # Empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        removed = self.head
        if self.head == self.tail:  # One element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed.value

    def remove_tail(self):
        if self.tail is None:
            return None
        removed = self.tail
        if self.head == self.tail:  # One element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed.value

dll = DoublyLinkedList()
dll.add_to_head(10)
dll.add_to_tail(20)
dll.add_to_tail(30)

print(dll.remove_head())  # Output: 10
print(dll.remove_tail())  # Output: 30
```

Key Operations

Insertion

At head (O(1))

At tail (O(1))

Before/after a given node (O(1) with pointer)

Deletion

Remove head

Remove tail

Remove from middle (requires updating two neighbors)

Traversal

Forward traversal (head → tail)

Backward traversal (tail → head)

Advantages

Bidirectional traversal

Efficient insertions and deletions at both ends

Disadvantages

Requires more memory per node (extra pointer)

Slightly more complex to implement

Key Points to Remember

DLL nodes contain data, next, prev.

Supports traversal in both directions.

Adding/removing at head and tail is efficient.

Extra memory overhead compared to singly linked lists.