class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dict = collections.defaultdict(list)

        for i, parent in enumerate(ppid):
            dict[parent].append(pid[i])

        q = collections.deque([kill])
        res = []

        while q:
            kill = q.popleft()
            res.append(kill)
            if kill in dict:
                q += dict[kill]

        return res


"""
    time = O(n)
    space = O(n)
    hash + bfs
    
    create a hash first, default value being list
    
    iterate through parent(ppid):
        dict[parent] appends pid[i]
        
    create a queue using collections.deque, add input kill in it
    
    iterate through queue:
        kill = q.popleft()
        append kill to res
        if kill is in dictionary, add value to queue
        
    return res
"""
