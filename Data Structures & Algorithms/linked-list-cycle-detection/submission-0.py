# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if slow:
                slow = slow.next
            for _ in range(2):
                if fast:
                    fast = fast.next
        if fast and slow:
            return True
        return False

