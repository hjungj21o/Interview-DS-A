class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        while len(res) < numRows:
            sub = []
            for i in range(len(res) + 1):
                if i == 0 or i == len(res):
                    sub.append(1)
                else:
                    sub.append(res[-1][i - 1] + res[-1][i])
            res.append(sub)

        return res


"""
    create empty list, res
    
    create a while loop so that length of res doesn't exceed input numRows
        create empty list, sub
        for loop to iterate through length of res
            if i == 0 or i == length of res, append 1 to sub
            else, append res[-1]'s i - 1 and i to sub
        after the loop is done, append sub to res
        
    return res

"""
