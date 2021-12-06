import numpy as np

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

with open('garrett\day5\d5p1-input.txt', 'r') as f:
    data = f.readlines()

data = [x.split() for x in data]

#creates an array of line objects
lines = []
for x in data:
    point1 = list(map(int, x[0].split(',')))
    point2 = list(map(int, x[2].split(',')))
    lines.append(Line(point1, point2))

#gets the largest values and then creates an array of that size
maxX, maxY = 0, 0
for l in lines:
    if l.start[0] > maxX: maxX = l.start[0]
    if l.end[0]   > maxX: maxX = l.end[0]
    if l.start[1] > maxY: maxY = l.start[1]
    if l.end[1]   > maxY: maxY = l.end[1]
lineChart = np.zeros((maxY + 1, maxX + 1))

def plotDiag(x, line, lineChart):
    #print('x: %d (%d, %d) -> (%d, %d)' % (x, line.start[0],line.start[1],line.end[0],line.end[1]))
    #line points up and left
    if line.start[0] > line.end[0] and line.start[1] > line.end[1]:
        #print('up and left')
        for i in range(x + 1):
            lineChart[line.end[1] + i][line.end[0] + i] += 1
    
    #line points up and right
    elif line.end[0] > line.start[0] and line.start[1] > line.end[1]:
        #print('up and right')
        for i in range(x + 1):
            lineChart[line.end[1] + i][line.start[0] + i] += 1

    #line points down and left
    elif line.start[0] > line.end[0] and line.end[1] > line.start[1]:
        #print('down and left')
        for i in range(x + 1):
            lineChart[line.start[1] + i][line.end[0] + i] += 1
    
    #line points down and right
    else:
        #print('down and right')
        for i in range(x + 1):
            lineChart[line.start[1] + i][line.start[0] + i] += 1

def plot(line, chart):
    #gets change in x and y
    x = abs(line.start[0] - line.end[0])
    y = abs(line.start[1] - line.end[1])

    #plots the diaganal line and returns
    if x == y: 
        plotDiag(x, line, lineChart)
        return

    #horozontal line
    if x > 0:
        #line goes from right to left
        if line.start[0] > line.end[0]:
            for i in range(x + 1):
                chart[line.start[1]][line.end[0] + i] += 1
        #line goes from left to right
        else:
            for i in range(x + 1):
                chart[line.start[1]][line.start[0] + i] += 1
    
    #vertical line
    else:
        #line goes from bottom to top
        if line.start[1] > line.end[1]:
            for i in range(y + 1):
                chart[line.end[1] + i][line.start[0]] += 1
        #line goes from top to bottom
        else:
            for i in range(y + 1):
                chart[line.start[1] + i][line.start[0]] += 1

#plots all the lines
for line in lines:
    plot(line, lineChart)

#counts the number of points with overlapping lines
count = 0
for i in range(len(lineChart)):
    for j in range(len(lineChart[i])):
        if lineChart[i][j] > 1: count += 1

print(count)