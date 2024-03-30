class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calculate_gcd(a, b):
            return a if b == 0 else calculate_gcd(b, a % b)
        if not head or not head.next:
            return head

        temp1, temp2 = head, head.next
        while temp2:
            num1, num2 = temp2.val, temp1.val
            gcd_result = calculate_gcd(num1, num2)
            new_node = ListNode(gcd_result)
            temp1.next = new_node
            new_node.next = temp2
            temp1 = temp2
            temp2 = temp2.next
    
        return head