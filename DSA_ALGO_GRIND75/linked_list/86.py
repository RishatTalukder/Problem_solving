# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        greater_than_eql = ListNode()
        greater_than_eql_head = greater_than_eql
        prev = dummy = ListNode()
        dummy.next = head
        while head:
            if head.val >= x:
                greater_than_eql.next = head
                greater_than_eql = greater_than_eql.next
            else:
                prev.next = head
                prev = prev.next

            head = head.next

        greater_than_eql.next = None
        prev.next = greater_than_eql_head.next

        return dummy.next
