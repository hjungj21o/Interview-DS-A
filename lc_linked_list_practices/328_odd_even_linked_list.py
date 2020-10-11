# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


"""
    Pseudocode:
    create two var, odd and even, odd starting at head and even starting at head.next
    create one more var pointing to even (so that we can attach even to the end of odd later)
    iterate through the linked list until we get to the end of even
        odd.next becomes even.next (skip), advance odd
        even.next becomes odd.next (skips odd), advance even
        
    attach even to the end of odd
    return head
"""
