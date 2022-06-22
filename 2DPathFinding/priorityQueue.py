import itertools
import heapq

#Parts of code taken from https://docs.python.org/3.8/library/heapq.html
class PriorityQueue:
    def __init__(self):
        self.pq = []                         
        self.entry_finder = {}               
        self.REMOVED = '<removed-task>'      
        self.counter = itertools.count()     

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
    
    def contains(self, state):
        return state in self.entry_finder

    def length(self):
        return len(self.pq)

    def get_priority(self, task):
        if task in self.entry_finder:
            return self.entry_finder[task][0]
        else:
            return float("inf")