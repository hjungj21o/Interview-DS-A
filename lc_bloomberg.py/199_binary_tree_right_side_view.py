# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1, 2, 3, null, 5, null, 4]
# Output: [1, 3, 4]
# Explanation:

#    1 < ---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                curr = queue.popleft()

                if i == size - 1:
                    res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res


"""
    create a result list
    create a queue using collections.deque, add root to it
    
    while queue (traversing through the tree):
        get the size of the queue
        iterate through the range of size
            curr = popleft()
            if i is at the end of the queue(size - 1):
                append curr.val to res list
            if left exists, append left to queue
            same with right
    
    return res
"""
