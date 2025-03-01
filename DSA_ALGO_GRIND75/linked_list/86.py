# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        ge = ListNode()
        ge_head = ge
        prev = dummy = ListNode()
        dummy.next = head
        while head:
            if head.val >= x:
                ge.next = head
                ge = ge.next
            else:
                prev.next = head
                prev = prev.next

            head = head.next

        ge.next = None
        prev.next = ge_head.next

        return dummy.next
