# Linked List

## Definition

A linked list is a linear data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node in the list.


Linked list is basically a chain of nodes where each node contains information such as data and a pointer to the next node in the chain.

## Types of Linked List

- Singly Linked List
- Doubly Linked List
- Circular Linked List

- Singly Linked List: A singly linked list is a linear data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node in the list.
- Doubly Linked List: A doubly linked list is a linear data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the previous and next node in the list.
- Circular Linked List: A circular linked list is a linear data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node in the list.

## Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

## Operations

- Insertion: Insert a new node at the beginning, end, or at a specific position in the list.
- Deletion: Delete a node from the list.
- Traversal: Traverse the list to access each node.
- Search: Search for a specific node in the list.
- Update: Update the data of a specific node in the list.
- Sort: Sort the list in ascending or descending order.
- Reverse: Reverse the list.
- Merge: Merge two lists into a single list.
- Split: Split the list into two lists.


# Fast and Slow Pointer

- Fast pointer: Moves two steps at a time.
- Slow pointer: Moves one step at a time.

- When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.
- When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.