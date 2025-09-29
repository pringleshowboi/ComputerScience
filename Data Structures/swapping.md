# Swapping in Linked Lists  

## Introduction  
Swapping in linked lists refers to the process of **exchanging nodes or their values** within the list.  
This operation is common in problems such as sorting, reordering, or pairwise swapping of nodes.  

---

## Types of Swapping  

### 1. Swapping Node Values  
- Only the **data** inside two nodes is exchanged.  
- Node positions in the list remain unchanged.  
- Simple to implement.  

### 2. Swapping Entire Nodes  
- The **links (pointers)** are rearranged so that nodes change position in the list.  
- More complex but necessary if node identity must be preserved.  

---

## Example: Swapping Node Values  

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

    def swap_values(self, node1, node2):
        if node1 and node2:
            node1.value, node2.value = node2.value, node1.value

ll = LinkedList()
ll.insert_beginning(10)
ll.insert_beginning(20)

first = ll.head
second = ll.head.next

#Swapping Nodes by Pointers

ll.swap_values(first, second)

print(first.value, second.value)  # Output: 10 20 (swapped)

def swap_nodes(head, val1, val2):
    if val1 == val2:
        return head

    prev1 = prev2 = None
    node1 = node2 = head

    # Find node1
    while node1 and node1.value != val1:
        prev1 = node1
        node1 = node1.next

    # Find node2
    while node2 and node2.value != val2:
        prev2 = node2
        node2 = node2.next

    # If either node not found, return unchanged list
    if not node1 or not node2:
        return head

    # Swap previous node pointers
    if prev1:
        prev1.next = node2
    else:
        head = node2

    if prev2:
        prev2.next = node1
    else:
        head = node1

    # Swap next pointers
    node1.next, node2.next = node2.next, node1.next

    return head

# Create linked list: 1 → 2 → 3 → 4
ll = LinkedList()
for val in [4, 3, 2, 1]:
    ll.insert_beginning(val)

# Swap nodes with values 2 and 3
ll.head = swap_nodes(ll.head, 2, 3)

# Expected list: 1 → 3 → 2 → 4
```
Key Considerations

Swapping values is simpler but does not preserve node identity.

Swapping nodes requires careful pointer updates to avoid breaking the list.

Special care is needed when swapping:

The head node

Adjacent nodes

When one or both nodes do not exist

Key Points to Remember

Two methods exist: swap values or swap nodes.

Swapping nodes is more complex but sometimes required.

Always handle edge cases: head, tail, and missing nodes.