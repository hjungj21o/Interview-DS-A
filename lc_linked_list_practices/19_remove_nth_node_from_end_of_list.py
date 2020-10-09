# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
