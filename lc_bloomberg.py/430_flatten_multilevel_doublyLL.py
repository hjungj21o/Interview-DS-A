"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        prev = Node(0, None, head, None)

        stack = [head]

        while stack:
            curr = stack.pop()

            curr.prev = prev
            prev.next = curr

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        head.prev = None
        return head


"""
    create a prev node with val 0, prev to None, next to Head, and child to None
        prev will help us keep track of the prev node so taht we can link it to next node
    
    create a stack, with head in it
    
    while stack:
        curr = pop
        
        curr.prev = prev
        prev.next = curr
        
        if next exists, append it to stack
        if child exists, append it to stack and point .child to None
        move prev along to curr
        
    
    unlink the dummy prev node from head (head.prev = None)
    
    return head

"""
