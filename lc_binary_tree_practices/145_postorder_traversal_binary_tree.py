# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
#         #recursive
#         if not root: return None
#         result = []
        
#         def dfs(node):
#             if node.left: dfs(node.left)
#             if node.right: dfs(node.right)
#             result.append(node.val)
            
#         dfs(root)
#         return result
    
#         stack = []
#         result = []
        
#         while stack or root:
#             if root:
#                 if root:
#                     if root.right: stack.append(root.right)
#                     stack.append(root.left)
#                     root = root.left
#                 else:
#                     root = stack.pop()
#                     result.append(root.val)
#                     root = root.left
                    
#             return result
    
        
        
"""
    postorder = left, right, root
    
    recursive:
        initialize a result arr
        define a new function, dfs, taking in node as an arg
            if there's node
                dfs on node.left
                dfs on node.right
                append node.val to result
        dfs on root
        return result
        
    iterative:

"""