"""
#876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Bruteforce
"""

find the length of the linked list by iterating from head to tail and count the length
run until length/2 return its value

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  # pyright: ignore[reportUndefinedVariable]
        current = head
        l = 0
        while current:
            current = current.next
            l+=1
        current = head
        for i in range((l//2)):
            current = current.next
        return current


# two pointer (slow & fast) 

"""
in two pointer one pointer will run slow 1 step at a time and the fast pointer run 2 times at a time (2 steps at time)

so in this case when fast ponter reaches the tail mathematically the slow poniter is half of the fast pointer
example

slow - fast
    1 - 2
    2 - 4
    3 - 6
    4 - 8
    5 - 10
    
example-2

two persons running on track to reach 5km race
person1 is running at 5km/hour
person2 is running at 10km/hour

While the person2 reaching the endline of 5km the person 1 is exactly half of the distance to person2
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  # pyright: ignore[reportUndefinedVariable]
        current = head
        slow , fast = current,current
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
