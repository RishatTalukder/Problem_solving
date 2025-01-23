# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        def findGCD(a, b):
            return gcd(a, b)
        
        dummy = head
        
        while head.next:
            prev = head
            next = head.next
            gcdVal = findGCD(head.val, head.next.val)
            newNode = ListNode(gcdVal)
            prev.next = newNode
            newNode.next = next
            head = head.next.next

        return dummy 