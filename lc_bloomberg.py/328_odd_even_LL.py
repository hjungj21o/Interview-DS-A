# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #edge case:
        if not head:
            return None

        #create two vars, even and odd
        odd, even = head, head.next
        #create an even head that points to even's head
        even_head = even

        #create a loop, till even reaches end
        while even and even.next:
            #swap odd's next to even's next, advance
            odd.next = even.next
            odd = odd.next
            #swap even's next to odd's next
            even.next = odd.next
            even = even.next

        #connect odd.next to even_head
        odd.next = even_head

        return head


"""
    two pointers - even and odd
    create two vars, even and odd - odd pointing to head, and even pointing to head.next
    create another var, pointing to the beginning of even
    create a loop - until even reaches the end (since it's going to be ahead of odd)
        odd.next = even.next (even.next means it's odd) and advance odd
        even.next = odd.next (odd.next means it's even) and advance even    
    point odd's next to even_head
    return head
    edge case: if there's no head, return None
    time = 
    space = 
    
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


"""
    create an odd and even pointer, pointing to head and head.next
    head will act as the beginning of odd list
    create an evenhead & act as begin of even list
    
    iterate until even reaches the end (while even and even.next):
        odd.next = even.next
        odd = odd.next
        
        same with even
        
    after it has iterated through, odd.next should be evenhead
    
    return head(beginning of odd list)

"""
