# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dict = {}

        curr = head

        while curr:
            dict[curr] = ListNode(curr.val)
            curr = curr.next

        curr = head

        while curr:
            dict[curr].next = dict[curr.next] if curr.next else None
            dict[curr].random = dict[curr.random] if curr.random else None
            curr = curr.next

        return dict[head]


"""
    deep copy = new node with val, next, and rand taken from input
    
    create a dict, where it will house all new ListNodes
    
    curr will point to head
    
    iterate through curr, key being curr, value being new ListNode(curr.val)
    
    turn curr back to head
    
    iterate through curr again
        dict[curr].next = dict[curr.next]
        dict[curr].random = dict[curr.random]
        
    return dict[head]

"""
