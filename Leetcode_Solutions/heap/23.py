# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.heap = []
        for i, head in enumerate(lists):
            while head:
                heapq.heappush(self.heap, head.val)
                head = head.next
        
        dummy = ListNode(-1)
        head = dummy
        while self.heap:
            head.next = ListNode(heapq.heappop(self.heap))
            head = head.next


        return dummy.next