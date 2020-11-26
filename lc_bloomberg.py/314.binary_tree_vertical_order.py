# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        #         if not root: return None

        #         queue = deque()
        #         queue.append((root, 0))
        #         dict = collections.defaultdict(list)

        #         while queue:
        #             node, col = queue.popleft()

        #             if node:
        #                 dict[col].append(node.val)

        #                 queue.append((node.left, col - 1))
        #                 queue.append((node.right, col + 1))

        #         res = sorted([(k, v) for k, v in dict.items()], key=lambda x: x[0])
        #         return [i[1] for i in res]

        if not root:
            return None
        queue = deque()
        queue.append((root, 0))
        col_table = collections.defaultdict(list)
        min_val = float('inf')
        max_val = float('-inf')

        while queue:
            node, col = queue.popleft()

            if node:
                min_val = min(min_val, col)
                max_val = max(max_val, col)

                col_table[col].append(node.val)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [col_table[x] for x in range(min_val, max_val + 1)]


"""
    suboptimal way:
        hash, queue, and sorting
        
        build a dict with default value being a list
        build a queue, with root and column value (starting at 0)
        
        while queue:
            unpack popleft as node, col
            
            if node exists:
                add it to dict, with key being col and value being node.val
                
                add node.left nad col - 1 to node.left
                add node.right and col + 1 to node.right
                
        build a res var that contains a tuple of k,v. then sort it by the first ele
        return res[0]
        
    optimal way:
        hash, queue, keep min_val and max_val
        
        build a dict with default value being a list
        build a queue with root and col value (0 to start)
        min_val = inf
        max_val = -inf
        while queue:
            unpack popleft as node, col
            
            if node:
                get min between min_val and col
                get max between max_val and col
                add node.val with key col
                
                add node.left col - 1
                add node.right col + 1
        
        return [res[x] for x in range(min_val, max_val + 1)]

"""
