class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        size = len(self.list)
        self.list.append(val)
        self.dict[val] = size
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_ele, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_ele] = last_ele, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


"""
    Dict = O(1) insertion & deletion. Problems with GetRandom
    List = O(1) insertion & getrandom, but problem with deletion
    
    initialize dict & list
    
    insert:
        if value is in dict already, return False
        set dict[val] to size of list (0 when beginning)
        append val to list
        return True
        
    remove:
        if val is in dictionary:
            get the index of element to delete from dict as well as the last element in list
            move the last element to the place idx of the element to delete
            pop the last element
            del self.dict[val]
            return True
        return False
    
    getRandom:
        return choice(self.list)

"""


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
