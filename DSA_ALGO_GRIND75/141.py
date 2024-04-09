# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Check if a linked list has a cycle.
        
        This function uses the "two pointers" approach to determine if a linked list has a cycle.
        It starts by initializing two pointers: `slow` and `fast`, both pointing to the head of the linked list.
        Then, it enters a loop that continues until either `fast` reaches the end of the list or `fast` reaches a node that is the same as `slow`.
        Inside the loop, `slow` moves one step forward, while `fast` moves two steps forward.
        If at any point `slow` and `fast` point to the same node, it means that there is a cycle in the linked list, and the function returns True.
        If the loop ends without finding a cycle, it means that the linked list is acyclic, and the function returns False.
        
        Args:
            head (Optional[ListNode]): The head of the linked list.
        
        Returns:
            bool: True if the linked list has a cycle, False otherwise.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False