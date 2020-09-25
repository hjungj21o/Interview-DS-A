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

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]

        while len(stack):
            node, lob, upb = stack.pop()
            if node.val <= lob or node.val >= upb:
                return False

            if node.left:
                stack.append((node.left, lob, node.val))
            if node.right:
                stack.append((node.right, node.val, upb))

        return True
