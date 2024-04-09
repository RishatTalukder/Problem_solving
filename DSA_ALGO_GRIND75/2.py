# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
                Adds two numbers represented as linked lists.
        
                Args:
                    l1 (ListNode): The head of the first linked list.
                    l2 (ListNode): The head of the second linked list.
        
                Returns:
                    ListNode: The head of the resulting linked list.
        
                Description:
                    This function takes two linked lists, `l1` and `l2`, which represent two numbers. The function adds the numbers
                    together, digit by digit, and returns the result as a new linked list.
        
                    The function initializes a dummy head node and a tail node to keep track of the resulting linked list. It also
                    initializes a `carry` variable to keep track of any carry-over digits.
        
                    The function then iterates through the linked lists, adding the corresponding digits along with the carry. If
                    one of the linked lists ends before the other, a default value of 0 is used for the missing digits.
        
                    The sum of the digits and carry is calculated, and a new node with the resulting digit is created. This node is
                    appended to the tail of the resulting linked list, and the tail is updated to point to the new node.
        
                    After the iteration is complete, if there is still a carry-over digit, a new node is created and appended to the
                    tail of the resulting linked list.
        
                    Finally, the dummy head node is disconnected from the resulting linked list, and the head of the resulting
                    linked list is returned.
        
                Complexity Analysis:
                    - Time Complexity: O(max(n, m)), where n and m are the lengths of the two input linked lists.
                    - Space Complexity: O(max(n, m)), as the resulting linked list can have a maximum length of max(n, m) + 1.
                """        
        
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result