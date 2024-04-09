# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temphead = head
        length = 1
        while temphead.next:
            temphead = temphead.next
            length += 1

        for i in range(k % length):
            dummy = ListNode(0, head)
            tail = head
            while tail.next.next:
                tail = tail.next

            temp = tail.next
            tail.next = None
            dummy.val = temp.val
            head = dummy

        return head
