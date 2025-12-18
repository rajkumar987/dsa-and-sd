# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        cur = None
        left = head
        right = head

        while k>1:
            right= right.next
            k-=1
        cur = right
        
        while right.next:
            right= right.next
            left = left.next
        cur.val ,left.val = left.val,cur.val
        return head
        