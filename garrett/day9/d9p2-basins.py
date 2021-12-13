topMap = [x.rstrip('\n') for x in open('garrett\day9\\testimput.txt', 'r')]

#calculates and returns the size of the basin
def getBasinSize(x, y, topMap, visitedPoints):
    size = 1

    #checks if the value is an edge point
    def edgeStop(direction):
        val = False
        if direction == 'w':
            if x == 1: pass
            elif topMap[y][x - 1] >= topMap[y][x - 2]: val = True
        
        if direction == 'e':
            if x == len(topMap[y]) - 2 or x == len(topMap[y]) - 1: pass
            elif topMap[y][x + 1] >= topMap[y][x + 2]: val = True
        
        if direction == 'n':
            if y == 1: pass
            elif topMap[y - 1][x] >= topMap[y - 2][x]: val = True
        
        if direction == 's':
            if y == len(topMap) - 2 or y == len(topMap) - 1: pass
            elif topMap[y + 1][x] >= topMap[y + 2][x]: val = True
        
        return val

    #checks west
    if x == 0 or (x - 1, y) in visitedPoints or edgeStop('w'): pass
    elif topMap[y][x] < topMap[y][x - 1]: 
        #print('moving to ', x-1, y)
        visitedPoints.append((x - 1, y))
        size += getBasinSize(x - 1, y, topMap, visitedPoints)

    #checks east
    if x == len(topMap[y]) - 1 or (x + 1, y) in visitedPoints or edgeStop('e'): pass
    elif topMap[y][x] < topMap[y][x + 1]: 
        #print('moving to ', x+1, y)
        visitedPoints.append((x + 1, y))
        size += getBasinSize(x + 1, y, topMap, visitedPoints)

    #checks north
    if y == 0 or (x, y - 1) in visitedPoints or edgeStop('n'): pass
    elif topMap[y][x] < topMap[y - 1][x]: 
        #print('moving to ', x, y-1)
        visitedPoints.append((x, y - 1))
        size += getBasinSize(x, y - 1, topMap, visitedPoints)
        
    #checks south
    if y == len(topMap) - 1 or (x, y + 1) in visitedPoints or edgeStop('s'): pass
    elif topMap[y][x] < topMap[y + 1][x]: 
        #print('moving to ', x, y+1)
        visitedPoints.append((x, y + 1))
        size += getBasinSize(x, y + 1, topMap, visitedPoints)

    return size

lowPoints = []
for y in range(len(topMap)):
    for x in range(len(topMap[y])):
        lowCount = 0
        #checks west
        if x == 0: lowCount += 1
        elif topMap[y][x] < topMap[y][x - 1]: lowCount += 1

        #checks east
        if x == len(topMap[y]) - 1: lowCount += 1
        elif topMap[y][x] < topMap[y][x + 1]: lowCount += 1

        #checks north
        if y == 0: lowCount += 1
        elif topMap[y][x] < topMap[y - 1][x]: lowCount += 1

        #checks south
        if y == len(topMap) - 1: lowCount += 1
        elif topMap[y][x] < topMap[y + 1][x]: lowCount += 1

        #incrament
        if lowCount == 4: lowPoints.append((x, y))


print(lowPoints)
biggest = 0
for point in lowPoints:
    biggest = getBasinSize(point[0], point[1], topMap, [])
    print(biggest)

