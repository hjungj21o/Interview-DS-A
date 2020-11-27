# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        carry = 0

        curr = l1

        while curr:
            s1.append(curr.val)
            curr = curr.next

        curr = l2

        while curr:
            s2.append(curr.val)
            curr = curr.next

        dummy = None

        while s1 or s2:
            pop1 = s1.pop() if s1 else 0
            pop2 = s2.pop() if s2 else 0
            val = pop1 + pop2 + carry
            dummy = ListNode(val % 10, dummy)
            carry = val // 10

        if carry:
            dummy = ListNode(carry, dummy)

        return dummy


"""
    2 stacks
    
    append l1 to 1 stack, l2 to stack 2
    
    create dummy node
    curr = dummy
    carry = 0 
    while s1 or s2:
        pop the value from s1 and s2
        val = popped1 + popped2 + carry
        
        curr.next = ListNode(val % 10, curr)
        carry = val // 10
        curr = curr.next
    
    return dummy.next
        
"""
