# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            temp = head
            after = head.next
            while after:
                if temp.val == after.val:
                    temp.next = after.next
                    after = after.next

                else:
                    temp = temp.next
                    after = after.next
            
            return head
        
        return head
            