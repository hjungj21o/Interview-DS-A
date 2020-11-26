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
