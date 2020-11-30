class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

#         target = len(graph) - 1
#         res = []

#         def backtrack(currNode, path):
#             if currNode == target:
#                 res.append(list(path))
#                 return

#             for nextNode in graph[currNode]:
#                 path.append(nextNode)
#                 backtrack(nextNode, path)
#                 path.pop()

#         path = [0]
#         backtrack(0, path)

#         return res
        target = len(graph) - 1
        res = []

        queue = deque()
        queue.append([0])

        while queue:
            top = queue.popleft()

            if top[-1] == target:
                res.append(top)
            else:
                for i in graph[top[-1]]:
                    queue.append(top + [i])

        return res
