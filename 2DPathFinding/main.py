from AStarFrontier import aStarSearch, grid
import random

if __name__ == '__main__':
    #Phase 1
    obstacles = [[9,7], [8,7], [6,7], [6,8]]
    gridVar = grid(obstacles)
    finalNode = aStarSearch(gridVar, (0,0), (9,9))
    if finalNode is None:
        print("Unable to reach delivery point\n")
    else:
        path = []
        node = finalNode
        steps = 0
        while node.parentNode is not None:
            path.append(node.location)
            location = node.location
            steps = steps + 1
            node = node.parentNode
            
        state = node.location
        gridVar[state[0]][state[1]] = 'X'
        path.reverse()
        print("Steps taken: " + str(steps))
        print("Path taken: " + str(path))

    #Phase 2
    for i in range(20):
        xCoords = random.randint(0, 9)
        yCoords = random.randint(0, 9)
        if (xCoords == 0 and yCoords == 0) or (xCoords == 9 and yCoords == 9) or ([xCoords, yCoords] in obstacles):
            while((xCoords == 0 and yCoords == 0) or (xCoords == 9 and yCoords == 9)  or ([xCoords, yCoords] in obstacles)):
                xCoords = random.randint(0, 9)
                yCoords = random.randint(0, 9)
        obstacles.append([xCoords, yCoords])
    print("Generated obstacles: " + str(obstacles))
    gridVar = grid(obstacles)
    finalNode = aStarSearch(gridVar, (0,0), (9,9))
    if finalNode is None:
        print("Unable to reach delivery point\n")
    else:
        path = []
        node = finalNode
        steps = 0
        while node.parentNode is not None:
            path.append(node.location)
            location = node.location
            steps = steps + 1
            node = node.parentNode
            
        state = node.location
        gridVar[state[0]][state[1]] = 'X'
        path.reverse()
        print("Steps taken: " + str(steps))
        print("Path taken: " + str(path))


