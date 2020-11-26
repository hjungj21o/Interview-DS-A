     costs.sort(key=lambda x: (x[0]-x[1]))
      res = 0
       for i in range(len(costs)//2):
            res += costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            res += costs[i][1]
        return res

"""
    sort by the difference between the two costs
    
    iterate through the half of the length of the array from the beginning
        increment result int by city A cost
    iterate through the 2nd half of costs array
        increment result int by city B cost
        
    return result


    [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    [[259,770],[184,139],[577,469],[926,667],[448,54],[840,118]]
       -511       45         90        220.      400.     680
"""
