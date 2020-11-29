# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque([root])
        level = 0
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)

        return res

        # if not root:
        #     return []
        # ans, level = [], [root]
        # while level:
        #     ans.append([node.val for node in level])
        #     temp = []
        #     for node in level:
        #         temp.extend([node.left, node.right])
        #     level = [leaf for leaf in temp if leaf]
        # return ans
