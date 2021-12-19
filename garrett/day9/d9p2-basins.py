topMap = [x.rstrip('\n') for x in open('garrett\day9\d9-input.txt', 'r')]

#calculates and returns the size of the basin plus one
def getBasinSize(x, y, topMap, visitedPoints):
    size = 1

    #checks west
    if x == 0 or (x - 1, y) in visitedPoints: pass
    elif topMap[y][x - 1] < '9': 
        visitedPoints.append((x - 1, y))
        size += getBasinSize(x - 1, y, topMap, visitedPoints)

    #checks east
    if x == len(topMap[y]) - 1 or (x + 1, y) in visitedPoints: pass
    elif topMap[y][x + 1] < '9': 
        visitedPoints.append((x + 1, y))
        size += getBasinSize(x + 1, y, topMap, visitedPoints)

    #checks north
    if y == 0 or (x, y - 1) in visitedPoints: pass
    elif topMap[y - 1][x] < '9': 
        visitedPoints.append((x, y - 1))
        size += getBasinSize(x, y - 1, topMap, visitedPoints)
        
    #checks south
    if y == len(topMap) - 1 or (x, y + 1) in visitedPoints: pass
    elif topMap[y + 1][x] < '9': 
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

#gets the sizes of all the basins in the map
sizes = []
for point in lowPoints:
    sizes.append(getBasinSize(point[0], point[1], topMap, []) - 1)

#sums the largest three elements
sum = 1
for i in range(3):
    index = sizes.index(max(sizes))
    sum *= sizes.pop(index)

print(f'the sum is {sum}')

