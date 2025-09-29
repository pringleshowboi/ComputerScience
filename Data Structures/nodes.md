# Nodes in Data Structures  

## Introduction  
A **node** is the fundamental building block of many data structures, including linked lists, trees, and graphs.  
It acts as a container that stores **data** and may also include one or more **pointers (or references)** to connect with other nodes.  

---

## Structure of a Node  

A typical node contains:  
- **Data** → the value or information stored in the node.  
- **Pointer(s)** → reference(s) to other node(s).  

For example, in a **singly linked list**, each node has:  
- `data`  
- `next` → pointer to the next node  

In a **doubly linked list**, each node has:  
- `data`  
- `next` → pointer to the next node  
- `prev` → pointer to the previous node  

---

## Node Representation in Python  

```python
class Node:
    def __init__(self, value):
        self.value = value      # Data stored in the node
        self.next = None   
             # Pointer to the next node (default: None)
# Creating nodes
node1 = Node(5)
node2 = Node(10)

# Linking nodes
node1.next = node2

# Traversing
print(node1.value)      # Output: 5
print(node1.next.value) # Output: 10
```

Key Points to Remember

A node is a container for data + pointer(s).

Nodes enable the creation of dynamic data structures.

In linked lists, nodes are connected sequentially.

In trees and graphs, nodes may have multiple connections.