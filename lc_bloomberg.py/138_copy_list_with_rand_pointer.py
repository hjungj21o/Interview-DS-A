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
