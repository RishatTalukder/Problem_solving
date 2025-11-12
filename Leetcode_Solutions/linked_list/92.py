# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev_node = dummy
        curr = head

        dummy.next = head

        for _ in range(left-1):
            prev_node = prev_node.next 
            curr = curr.next 

        prev= None

        for _ in range(right-left+1):
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node

        prev_node.next.next = curr
        prev_node.next = prev

        return dummy.next