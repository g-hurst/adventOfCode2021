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
        if [point[0], point[1]] not in newPoints: newPoints.append(point)
        
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
        
    #gets the new set of points after the fold
    points = fold(folds[0][0], folds[0][1], points)
    
    print('total points:', len(points))
