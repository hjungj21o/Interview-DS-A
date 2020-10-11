# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #         sets = set()

        #         curr = headA
        #         while curr:
        #             sets.add(curr)
        #             curr = curr.next

        #         curr = headB
        #         while curr:
        #             if curr in sets: return curr
        #             curr = curr.next
        #         return None
        #instantiate two curr vars
        currA, currB = headA, headB
        #loop to see if there's a intersection
        while currA != currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next

        return currA


"""
    Pseudocode:
    instantiate two curr var pointing to both headA and headB respectively
    create a loop to see if there's a coinciding place (either a node or None)
    switch the heads when they are at the end
    return one of the currs, as it'll return either None or a node
"""


