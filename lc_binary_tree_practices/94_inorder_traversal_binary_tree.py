# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #         #recursive
        #         result = []

        #         def dfs(node):
        #             if node:
        #                 dfs(node.left)
        #                 result.append(node.val)
        #                 dfs(node.right)

        #         dfs(root)
        #         return result

        #iterative
        #initialize result arr
        result = []
        #initialize stack (abstract data type - LIFO)
        stack = []

        #we traverse as long as there's untravelled node(stack is not empty)
        #or while we're at a valid node
        while stack or root:
            if root:
                #if we're at a valid node, save it to the stack (where we've been)
                #and keep moving down left
                stack.append(root)
                root = root.left
            else:
                #if we're here, that means we've hit a dead end, so...
                #pop the most recent node we've travelled to
                #append the value to the results arr
                #keep moving right now
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result


"""
    inorder = left, root, right
    iterative:
        create result and stack vars
        traverse through the tree (while stack is not empty or if there's a root):
            if root exists (root will now be traversing down all the way to the left side)
                append it to the stack
                root becomes root.left
            else (which means we've now went all the way to the left)
                we set the root to the popped node from the stack
                append it to the result array
                root becomes root.right
            
    recursive:
        create result arr 
        define new function dfs, take in node as arg
            if node exists, then go through all of node.left
            append node.val to result
            go through all of node.right
        
        dfs on root
        return result
"""
