# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        max_depth = 1
        while stack:
            node, depth = stack.pop()

            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
            max_depth = max(max_depth, depth)
        return max_depth


"""
    Gotta keep track of max depth as we're traversing down to the leaf
    
    create a stack and define max depth, starting at 1
    traverse through the tree via stack
        deconstruct node and depth from the popped node from stack
        
        append the node.left and node.right to stack if they exist
        get the max depth by comparing max depth and the current depth
        
    return max depth
"""
