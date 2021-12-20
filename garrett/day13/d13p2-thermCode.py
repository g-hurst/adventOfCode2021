#folds the points and then returns updated points
def fold(axis, val, points):
    #fold across an x equals line
    if axis == 'x': 
        for point in points:
            if point[0] > val:
                point[0] -= 2 * (point[0] - val)
                
    #fold across a y equals line
    elif axis == 'y': 
        for point in points:
            if point[1] > val:
                point[1] -= 2 * (point[1] - val)
                
    #fold is neither x or y
    else: print('unknown fold')
    
    #removes the duplicate points
    newPoints = []
    for point in points:
        if point not in newPoints: newPoints.append(point)
        
    return newPoints


if __name__ == '__main__':
    #gets the data
    data = [x.rstrip('\n') for x in open('garrett\day13\d13-input.txt', 'r')]

    points = []
    folds = []

    #turns the data into more workable lists
    splitIndex = 0
    for i in range(len(data)): 
        if data[i] == '': 
            splitIndex = i + 1
            break
        points.append(list(map(int, data[i].split(','))))
    for i in range(splitIndex, len(data)): 
        axis, val = data[i].split()[2].split('=')
        folds.append((axis, int(val)))
        
    #completes all the folds
    for f in folds:
        points = fold(f[0], f[1], points)
    
    #gets the max values all the points and creates an array
    maxX = max([x[0] for x in points])
    maxY = max([y[1] for y in points])
    message = [[' ' for _ in range(maxX + 1)] for _ in range(maxY + 1)]
    
    #plots the points
    for point in points:
        message[point[1]][point[0]] = '#'
        
    #outputs the message to a file
    with open('garrett\day13\output.txt', 'w') as f:
        for line in message:
            outStr = ''.join(line) + '\n'
            f.write(outStr)