# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # 1. Find midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # 2. Reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Split the list in to 2 halves
        second = prev
        first = head


        # 4. Merged two halves
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        