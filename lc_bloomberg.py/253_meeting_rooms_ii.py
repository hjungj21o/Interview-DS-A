class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(list(i[0] for i in intervals))
        end = sorted(list(i[1] for i in intervals))

        e = 0
        rooms = 0

        for s in start:
            if s < end[e]:
                rooms += 1
            else:
                e += 1

        return rooms


"""
    What we care most about is if start time < end time, then there's a collision and to avoid collision, we'd need to increase the number of rooms
    
    sort start and end by their respective elements
    
    iterate through start:
        if s < end[e]:
            increment rooms
        else:
            increment e pointer
    
    return rooms

"""
