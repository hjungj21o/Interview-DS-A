# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        dummy = ListNode(0)
        p1, p2 = l1, l2
        curr = dummy
        step = 0
        while p1 or p2:
            num1 = p1.val if p1 is not None else 0
            num2 = p2.val if p2 is not None else 0
            num = num1 + num2 + step
            curr.next = ListNode(num % 10)
            step = num // 10
            curr = curr.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if step:
            curr.next = ListNode(step)

        return dummy.next


"""
    Pseudocode:
        instantiate a dummy node
        have a pointer each for l1 and l2
        create a step var (toggle between 1 or 0)
        iterate through BOTH lists
            if any of the values are None because it's at the end of the list, point it to 0
            curr.next should point to a new node that's been modded by 10 (if greater than 10, grab the last digit, if it's not, then it'll just return the number)
            divide the sum by 10 and point it to step (it will either be 0 or 1)
            move curr pointer
            if p1 exists, then move p1 pointer. Same with p2
        After the loop, if step is greater than 0, curr.next should point to a new Node with step as the value
        return dummy.next
"""
