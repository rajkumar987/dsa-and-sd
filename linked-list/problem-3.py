"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

# Bruteforce
"""

find the length of the linked list by iterating from head to tail and count the length
run until length-n return its value

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# solution 1
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # pyright: ignore[reportUndefinedVariable]
        current = head
        l = 0
        while current:
            current = current.next
            l+=1
        if n==l:
            return head.next
        current = head
        for i in range(l-n-1):
            current = current.next
        current.next = current.next.next
        return head


# solution2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # pyright: ignore[reportUndefinedVariable]
        if not head or not head.next:
            return head
        left = head
        right = head
        for _ in range(n):
            right = right.next
        if not right:
            head = head.next
            return head

        while right and right.next:
            left = left.next
            right = right.next
        if left:
            left.next = left.next.next
        return head