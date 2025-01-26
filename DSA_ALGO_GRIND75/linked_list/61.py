# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 1
        temp = head

        while temp.next:
            length += 1
            temp = temp.next

        k = k % length
        if k == 0:
            return head
    
        temp.next = head
        temp = head

        for _ in range(length - k - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        return new_head
