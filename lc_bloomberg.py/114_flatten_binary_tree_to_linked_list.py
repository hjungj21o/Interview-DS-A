# Given a binary tree, flatten it to a linked list in -place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            if stack:
                curr.right = stack[-1]

            curr.left = None


"""
    create stack with root in stack
    
    traverse through the tree inorder (append right, append left)
    
    if there's anything in the stack, then set curr.right to last element in stack
    
    set curr.left to None

"""
