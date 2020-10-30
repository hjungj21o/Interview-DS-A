# Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center).

# For example, this binary tree[1, 2, 2, 3, 4, 4, 3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isMirror(root, root)

    def isMirror(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left):
            return True


"""
    Recursion:
        need a helper function where it takes 2 args (2x root)
        helper function:
            3 conditions to check: 
                1. if l and r don't exist, it must mean they are mirrors. return true
                2. if l and r values are same, and when calling helper function recursively on both l.left, r.right and l.right and r.left are the same, then it must mean they are mirrors. return true
                3. if either l or r do not exist, that means they aren't mirrors. return false.
                
        main function:
            edge case: if there's no root, then return True
            call isMirror on 2 roots.

"""
