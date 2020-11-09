# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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


# Input: root = [1, 2, 3, 4, 5, 6, 7]
# Output: [1,  # ,2,3,#,4,5,6,7,#]


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

        queue = [root]
        count = 0
        limit = 1

        while queue:
            curr = queue.pop(0)
            count += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if count == limit:
                count = 0
                limit *= 2
                curr.next = None
            else:
                curr.next = queue[0]

        return root


"""
    use bfs (queue)
    
    create queue, add root to it
    create count, starting at 0 and limit at 1 (count is going to go towards limit, limit is going to double as we traverse down the level)
    
    using queue, traverse through the tree:
        curr = pop(0)
        increment count
        add left and right to the queue if they exist
        
        if count == limit (meaning we've reached the end of the level):
            reset count, double the limit, and set the curr.next to None (just to make sure)
        else:
            curr.next should be set to the first ele in queue
    
    return root
        
"""
