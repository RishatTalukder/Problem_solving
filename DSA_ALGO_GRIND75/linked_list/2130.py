from collections import deque

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        full_list = deque()

        while head:
            full_list.append(head.val)
            head = head.next
        
        maxx = 0
        while full_list:
            left = full_list.popleft()
            right = full_list.pop()
            maxx = max(maxx, left + right)

        return maxx

        

         