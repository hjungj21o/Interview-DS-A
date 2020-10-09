# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


"""
    Pseudocode:
    create a prev var, pointing towards none
    create a curr var, pointing at head
    create a loop to iterate through list
    create a next var, which will keep "record" of the rest of the list
    curr.val's next node should be pointed to prev
    move prev to curr node and curr to next
    return prev
"""
