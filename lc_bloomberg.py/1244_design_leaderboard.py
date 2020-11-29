class Leaderboard:

    def __init__(self):
        self.scores = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        tops = heapq.nlargest(K, self.scores.values())
        return sum(tops)

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]


"""
    Use a dictionary and maxheap
        dictionary = lookup O(1), so we can add the score with userID perfectly
            deletion O(1), so we can reset (delete) player's score efficiently
        
        heap:
            since dictionary is unordered, we can use heap's advantage to get the sum of top K players.
            building heap will be O(n log k)
            
        constructor:
            defaultdict(int)
            
        addScore:
            key = playerId, increment score
            
        top:
            sum up heapq.nlargest(K, values)
        
        reset:
            del self.scores[Id]
            

"""
