from priorityQueue import PriorityQueue
from node import Node

#adapted from A* search algorithm work through sheet from university
class Frontier:
    #frontier representing all nodes that we can travel to 
    def __init__(self, heuristic, goal, rootNode):
        self.heuristic = heuristic
        self.priorityQueue = PriorityQueue()
        self.locations = set()
        self.goal = goal

        if rootNode is not None:
            self.push(rootNode)
    
    #push if the node to be pushed if it hasn't been visited or has a lower cost than the same node in the priority queue
    def push(self, node):
        fn = heuristicCost(self.goal, node)
        if fn < self.priorityQueue.get_priority(node):
            self.priorityQueue.add_task(node, fn) #add node to priority queue with heuristic value
            self.locations.add(node.location)
        
    #pop node with highest priority
    def pop(self):
        node = self.priorityQueue.pop_task()
        self.locations.remove(node.location)
        return node
    
    def length(self):
        return self.priorityQueue.length()

def grid(obstacles):
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #apply obstacles to grid
    for obstacle in obstacles:
        grid[obstacle[0]][obstacle[1]] = 'X'

    return grid
    

def heuristicCost(goal, node):
    heuristicValue = node.totalCost + abs(goal.location[0] - node.location[0]) + abs(goal.location[1] - node.location[1]) #Manhattan distance as heuristic
    return heuristicValue

def aStarSearch(grid, start, goal):
    frontier = Frontier(0, Node(goal, None), Node(start, None))
    currentNode = frontier.pop()
    exploreNodes = set()

    while not currentNode.location == goal:
        currentLocation = currentNode.location
        exploreNodes.add(currentLocation)
        neighbourNodeLocations = []
        neighbourNodeLocations.append((currentLocation[0] + 1, currentLocation[1]))#up neighbour
        neighbourNodeLocations.append((currentLocation[0] - 1, currentLocation[1]))#down neighbour
        neighbourNodeLocations.append((currentLocation[0], currentLocation[1] + 1))#right neighbour
        neighbourNodeLocations.append((currentLocation[0], currentLocation[1] - 1))#left neighbour
        for neighbourNodeLocation in neighbourNodeLocations:
            #check neighbourNodes are within the size constraints of the grid and not an obstacle
            if 0 <= neighbourNodeLocation[0] < len(grid) and 0 <= neighbourNodeLocation[1] < len(grid[0]) and grid[neighbourNodeLocation[0]][neighbourNodeLocation[1]] != 'X':
                if neighbourNodeLocation not in exploreNodes: #if already explored, there is a shorter path to that node due to priority
                    node = Node(neighbourNodeLocation, currentNode)
                    frontier.push(node)

        if frontier.length() == 0:
            return None

        currentNode = frontier.pop()

    return currentNode


