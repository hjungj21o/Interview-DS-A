# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next


"""
    Pseudocode:
        create two vars, pointing to l1 and l2
        create a dummy node
        create a loop, iterating through the end of either l1 or l2
        if l1's val is greater, dummy.next becomes l2's val, and move l2 up
        vice versa for if l2 val is greater
        
        after the loop is over, dummy.next becomes either l1 or l2 (whatever is remaining)
        return dummy.next

"""
