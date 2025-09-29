# Two-Pointer Linked List Techniques  

## Introduction  
The **two-pointer technique** (also called the *runner technique*) is a common approach to solve linked list problems.  
It uses **two iterators** moving at different positions or speeds to efficiently find relationships between nodes.  

---

## Example Problem: Nth-to-Last Element  

**Problem:**  
Create a method that returns the *nth-to-last element* of a singly linked list.  

**Example:**  
Given the linked list:  

The 2nd-to-last element is **4**.  

---

## Naïve Approach (Extra Space)  

One possible approach:  
1. Traverse the linked list and store nodes in a list.  
2. Index into the list to get the nth-to-last element.  

### Implementation  

```python
def list_nth_last(linked_list, n):
    linked_list_as_list = []
    current_node = linked_list.head_node
    while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]

```
Complexity

Time: O(n)

Space: O(n) (extra memory for list storage)

Optimized Approach (Two Pointers)

We can solve the problem using two pointers moving at the same rate, with one pointer delayed by n steps.

```
nth_last = None
tail = linked list head
count = 1

while tail exists:
    move tail forward
    increment count

    if count >= n + 1:
        if nth_last is None:
            nth_last = head
        else:
            move nth_last forward

return nth_last
```
Visualization

We want the 2nd-to-last node in:
Steps:

Start: count = 1, T = head, N = None

Step 1: count = 2, T = node 2

Step 2: count = 3, T = node 3, N = node 1

Step 3: count = 4, T = node 4, N = node 2

Step 4: count = 5, T = node 5, N = node 3

Step 5: count = 6, T = None, N = node 4

```
from LinkedList import LinkedList

def nth_last_node(linked_list, n):
    nth_last = None
    tail = linked_list.head_node
    count = 1

    while tail:
        tail = tail.get_next_node()
        count += 1

        if count >= n + 1:
            if nth_last is None:
                nth_last = linked_list.head_node
            else:
                nth_last = nth_last.get_next_node()

    return nth_last

def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

# Test
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)  # Expected output: 47
```
Complexity Analysis

Time: O(n) (single pass through the list)

Space: O(1) (constant extra space, no auxiliary list)

Key Points to Remember

The two-pointer technique avoids extra space.

Useful for problems like:

Finding nth-to-last element

Detecting cycles in a list

Finding the middle element

Always consider edge cases:

n larger than list length

Empty list

n = 1 (last element)