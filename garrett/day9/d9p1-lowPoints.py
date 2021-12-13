topMap = [x.rstrip('\n') for x in open('garrett\day9\d9-input.txt', 'r')]

risk = 0
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
        if lowCount == 4: risk += int(topMap[y][x]) + 1

print('risk', risk)