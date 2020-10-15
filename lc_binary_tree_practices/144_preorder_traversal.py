# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #         #iterative
        #         if not root: return None
        #         result = []
        #         stack = [root]

        #         while stack:
        #             curr = stack.pop()

        #             result.append(curr.val)

        #             if curr.right:
        #                 stack.append(curr.right)
        #             if curr.left:
        #                 stack.append(curr.left)

        #         return result

        #recursive
        result = []

        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return result


"""
    preorder = root, left, right
    iterative:
        declare a result arr and stack arr. stack should already have root node inside
        traverse through the tree using stack (while stack is not none)
            pop the stack, append its value to result arr
            if there's a right, then append right to stack
            if there's a left, append left to stack --> we append right then left b/c stack is LIFO.
            
        return result
        
    recursive:
        declare a result arr var.
        define a dfs function via closure, taking in node as argument
            if node exists, append the value to result
            recursive call to node.left
            recursive call to node.right
        return result
"""
