# Given a binary tree, determine if it is a valid binary search tree(BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(node, lower=float('-inf'), higher=float('inf')):
            if not node:
                return True

            val = node.val

            if val <= lower or val >= higher:
                return False

            return helper(node.left, lower, val) and helper(node.right, val, higher)

        return helper(root)


"""
    recursion:
        need a helper function, takes in node, lower val and higher val. lower has default arg of -Inf and higher has default val of Inf
        
        if there's node (means we've traversed through all nodes without a hitch) return True
        
        if val <= lower or val >= higher (meaning the BST isn't valid): return False
        
        recursively call helper method on node.left with higher val replaced with node's val (b/c we don't want node.left.val >= higher) and node.right with lower val replaced with node's val

"""
