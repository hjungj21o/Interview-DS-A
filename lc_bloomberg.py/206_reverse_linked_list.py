# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


"""
    3 pointers
    
    prev points to None
    curr points to head
    
    iterate through input head via curr:
        save subsequent nodes via next variable
        curr.next = prev (reversing)
        prev = curr
        curr = next (moving through nodes)
    
    return prev (new head)
"""
