class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        half_list = []
        while fast and fast.next:
            half_list.append(slow)
            slow = slow.next
            fast = fast.next.next

        maxx = 0
        while slow:
            summ = slow.val + half_list.pop().val
            maxx = max(maxx,summ)

            slow = slow.next

        return maxx
         