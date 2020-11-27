class BrowserHistory:

    def __init__(self, homepage: str):
        self.list = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.list = self.list[:self.idx + 1]
        self.list.append(url)
        self.idx = len(self.list) - 1

    def back(self, steps: int) -> str:
        if self.idx - steps < 0:
            self.idx = 0
        else:
            self.idx -= steps
        return self.list[self.idx]

    def forward(self, steps: int) -> str:
        if steps + self.idx >= len(self.list):
            self.idx = len(self.list) - 1
        else:
            self.idx += steps

        return self.list[self.idx]


"""
    Thinking an array(list) would work here
    as long as you keep track of index, it's constant lookup & insertion. 
    
    in the constructor:
        get rid of forward history by resetting list to list[:idx + 1]
        self.list = [homepage inside]
        self.idx = 0
        
    in visit:
        set idx to len(list)
        append url to end of self.list
        
    in back:
        need if steps > this.idx:
            this.idx = 0
        else:
            idx -= steps
        return list[idx]

    forward:
        if steps > this.idx:
            this.idx = len(list) - 1
        else:
            idx += steps
            
        return list[idx]

"""


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
