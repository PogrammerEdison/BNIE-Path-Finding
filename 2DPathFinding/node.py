class Node:
    def __init__(self, location, parentNode):
        self.location = location
        self.parentNode = parentNode
        if parentNode is None:
            self.totalCost = 0
        else:
            self.totalCost = parentNode.totalCost + 1
    
    def __eq__(self, other):
        return self.location == other.location

    def __lt__(self, other):
        return self.location < other.location

    def __hash__(self):
        return hash(self.location)
    