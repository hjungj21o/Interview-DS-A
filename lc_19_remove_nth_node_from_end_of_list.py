# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1, 2], n = 1
# Output: [1]

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head

        first = second = dummy

        while n:
            first = first.next
            n -= 1
        # print(first.val)

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

    """
        Pseudocode:
        create a dummy node, connect it to head. 
        instantiate two variables, first and second, both starting at dummy
        create a loop by decrementing n, and let first traverse until n hits 0
        create another loop, going until first hits the end of list while having second traverse the list
        the second should reach the node before the one that needs to be removed. remove it
        return dummy.next
        
    """
