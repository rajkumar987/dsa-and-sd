# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if not head:
            return
        if not head.next:
            return head
        
        
        prev = None
        first = head
        second = head.next

        while first and second:
            if not prev:
                head = second
            else:
                prev.next = second
            
            temp = second.next
            second.next = first
            first.next = temp

            prev = first

            if temp and temp.next:
                first = temp
                second = temp.next
            else:
                break
        return head
        
        