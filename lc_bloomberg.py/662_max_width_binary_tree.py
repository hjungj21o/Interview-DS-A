# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            _, level_head_idx = queue[0]

            for i in range(len(queue)):
                node, col_idx = queue.popleft()

                if node.left:
                    queue.append((node.left, col_idx * 2))
                if node.right:
                    queue.append((node.right, col_idx * 2 + 1))

            max_width = max(max_width, col_idx - level_head_idx + 1)

        return max_width


"""
    BFS
    
    create a queue with root and its index in tuples
    create a max_width var starting at 0
    
    traverse through the tree via queue:
        unpack the index of queue[0]
        
        iterate through the current level (via length of current queue):
            unpack node and current column index with popleft
            
            if node.left: append node.left with index * 2
            if node.right: append node.right with index * 2 + 1
        
        get the max between max width and current index - head index + 1
        
    return max_width

"""
