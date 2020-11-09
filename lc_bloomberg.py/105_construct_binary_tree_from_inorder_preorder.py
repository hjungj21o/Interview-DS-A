# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        ele = preorder.pop(0)
        node = TreeNode(ele)
        idx = inorder.index(ele)
        node.left = self.buildTree(preorder, inorder[0:idx])
        node.right = self.buildTree(preorder, inorder[idx+1:])

        return node


"""
    get the first element fron preorder - that's the root
    make a node out of that
    get the index of popped ele in inorder - anything left of it will be node.left, anything right of that wil be node.right
        node.left = buildtree(inorder[0:idx])
        node.right = buildtree(inorder[idx+1:])
        
    return node
    
    if there's no preorder or inorder, then return None (base case)

"""
