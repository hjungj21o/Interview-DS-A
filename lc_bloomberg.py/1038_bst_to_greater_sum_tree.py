# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
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

        if not root:
            return None

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


"""
    Brute force? My intuition:
        Do an inorder traversal, store all the vals in a list
        build a queue, iterate through the queue, get the index of curr.val (popleft)
        update the val by adding up the inorder[idx:]
        
        append left and right to queue
        
        return root
        
        
    Optimal Solution:
        reverse inorder traversal
        
        declare a global/nonlocal val, starting at 0
        
        do a recursive dfs:
            recursively call on right first (we need the largest num first)
            val += node.val
            node.val = val
            do left
        
        dfs on root
        return root
"""
