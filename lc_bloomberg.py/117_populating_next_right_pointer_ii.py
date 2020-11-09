# Given a binary tree

# struct Node {
#     int val;
#     Node * left;
#     Node * right;
#     Node * next; }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.


# Follow up:

# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


# Example 1:


# Input: root = [1, 2, 3, 4, 5, null, 7]
# Output: [1,  # ,2,3,#,4,5,7,#]

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = collections.deque()
        queue.append(root)
        count = 0
        limit = 1

        while queue:
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1

            if count == limit:
                count = 0
                limit = len(queue)
                curr.next = None
            else:
                curr.next = queue[0]

        return root


"""
    similar to first one
    use queue
    
    use collections.deque to make a queue, append root
    create count at 0 and limit at 1
    
    traverse through the levels of tree with queue:
        curr = queue.popleft()
        
        append curr.left and curr.right 
        increment count
        
        if count == limit:
            reset count, reset limit to length of queue, and curr.next to None
        else:
            curr.next = queue[0]
            
        return root
    
"""
