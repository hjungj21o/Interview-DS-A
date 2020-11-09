# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        step = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + step

            curr.next = ListNode(val % 10)
            step = val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        if step:
            curr.next = ListNode(1)

        return dummy.next


"""
    two pointers
    create dummy node to return
    
    create a step that will toggle 1 or 0 depending on whether it goes over 10
    
    create a loop to iterate through both l1 and l2
        dummy.val = (l1.val + l2.val + step % 10) (if it's under 10, it'll still return same int)
        step = (l1.val + l2.val + step // 10)
        
    if step is 1 at the end, then dummy node's next = new node with 1 as the value
    
    return dummy head

"""
