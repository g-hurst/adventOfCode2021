import numpy as np

#stores input data
energyMap = np.array([[int(y) for y in x.rstrip('\n')] for x in open('garrett\day11\d11-input.txt', 'r')])
flashMap = np.zeros((len(energyMap), len(energyMap[0])))

def incrament(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] += 1

#gets the neighbors of a point in an array
def getNeighbors(point, arr):
    neighbors = []
    for xinc in range(-1, 2, 1):
        for yinc in range(-1, 2, 1):
            #you cant neighbor yourself
            if xinc == 0 and yinc == 0: continue
            x, y = point
            x += xinc
            y += yinc
            
            #checks to make sure the points are in bounds of the arr
            if x < 0 or y < 0: continue
            elif x > len(arr[0]) - 1 or y > len(arr) - 1: continue
            neighbors.append((x, y))
            
    return neighbors
     
#returns all the points where a flash should occur (val is > 9)
def getFlashPoints(arr):
    flashPositions = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > 9:
                flashPositions.append((j, i))
                
    return flashPositions
 
#updates the map with all the flashes and returns the number of flashes that occured
def updateMap(arr):
    #gets the flash positions and counts them
    flashPositions = getFlashPoints(arr)
    count = len(flashPositions)
        
    #updates the map incramenting the neighbors
    for point in flashPositions:
        neighbors = getNeighbors(point, arr)
        for pos in neighbors:
            x, y = pos
            #only incraments neighbors that have NOT just flashed
            if arr[y][x] > 0: arr[y][x] += 1
    
    #resets all the flashed points to zero
    for point in flashPositions: 
        x, y = point
        arr[y][x] = 0
    
    #recursive call in case any other points are flash ready
    if len(getFlashPoints(arr)) > 0: count += updateMap(arr)

    return count


if __name__ == '__main__':
    
    step = 0
    flashes = 0
    
    #incraments the step until a synchronous flash occurs
    while flashes != 100:
        incrament(energyMap)
        flashes = updateMap(energyMap)
        step += 1
    
    print('step of synchronized flashes:', step)

