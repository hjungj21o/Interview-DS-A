# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
#         inorder = []

#         def dfs(node):
#             if not node.left and not node.right:
#                 inorder.append(node.val)
#                 return inorder

#             if node.left:
#                 dfs(node.left)
#             inorder.append(node.val)
#             if node.right:
#                 dfs(node.right)

#         dfs(root)

#         queue = deque([root])

#         while queue:
#             curr = queue.popleft()
#             idx = inorder.index(curr.val)
#             curr.val = sum(inorder[idx:])

#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)

#         return root
        val = 0

        def dfs(node):
            nonlocal val
            if node.right:
                dfs(node.right)
            val += node.val
            node.val = val
            if node.left:
                dfs(node.left)
        dfs(root)
        return root
