# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        queue = deque([root])
        rev = False
        res = []

        while queue:
            temp = []
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                temp.append(curr.val)
                # print(i, curr.val, temp)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            rev = not rev
            if rev is False:
                temp.reverse()

            res.append(temp)

        return res


"""
    Use BFS to travel tree in level order (reverse it on every other lvl)
    
    create a queue, add root in it
    create a boolean var that will make the level reverse or not
    
    while queue:
        create a temp list
        save size of queue
        loop through the range of size:
            popleft = curr
            append curr.val to temp list
            append left and right to queue
        
        toggle boolean to not boolean
        if boolean is False, reverse it.
        
        append temp to res list
        
    return res

"""
