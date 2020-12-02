class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.journey = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = {
            "station": stationName,
            "time": t
        }

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin = self.check_in[id]

        time_taken = t - checkin['time']

        path = checkin["station"] + stationName

        if path not in self.journey:
            self.journey[path] = {
                "total": time_taken,
                "count": 1
            }
        else:
            prev_total = self.journey[path]

            self.journey[path] = {
                'total': prev_total["total"] + time_taken,
                'count': prev_total["count"] + 1
            }

        self.check_in.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path = startStation + endStation
        return self.journey[path]['total'] / self.journey[path]['count']


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.journey = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = {
            "start": stationName,
            "in": t
        }

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        total_time = t - self.check_in[id]["in"]
        journey = self.check_in[id]["start"]+stationName
        if journey in self.journey:
            self.journey[journey]["total"] += total_time
            self.journey[journey]["count"] += 1
        else:
            self.journey[journey] = {
                "total": total_time,
                "count": 1
            }

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = startStation + endStation
        return self.journey[journey]["total"] / self.journey[journey]["count"]


"""
    i have to use id to grab the information i want
    
    in order to get average, i need to keep count of how many start station and end station count there was, as well as the time it took from start to finish
    
    need a dict for check in, id being the key and name and station being the values (dict or list? does it matter? since it'll be 2 elements, lookup will be O(1)). 
    
    need a dict for keeping track of count and times it took from A -> B. maybe the key can be startstation (grabbing from checkin[id]) + endstation (input), values being count (which will be incremented) and total time (time += t), then we can grab the average. 

"""

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
