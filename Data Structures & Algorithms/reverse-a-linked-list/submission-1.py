# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev = head.next
        else:
            return head
        if prev:
            curr = prev.next
        head.next = None
        while prev:
            prev.next = head
            head = prev
            prev = curr
            if curr:
                curr = curr.next
        
        return head
