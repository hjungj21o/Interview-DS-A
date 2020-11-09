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
            if l2.val > l1.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next


"""
    two pointers
    
    create a dummy node
    curr point to dummy
    
    create a loop to iterate through both l1 and l2
        if l2.val > l1.val:
            dummy.next = l1
            move l1 along
        vice versa for l2
        
    if there's any left over in l1 or l2, attach it to curr.next
    
    return dummy.next
"""
