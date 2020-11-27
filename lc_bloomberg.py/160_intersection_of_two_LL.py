# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1


"""
    two pointers
    create two vars, pointing to each input head
    create a loop which goes on until the pointers end up at the same place
    if p1's next is None, then point to headB, and vice versa
    return p1 or p2
"""
