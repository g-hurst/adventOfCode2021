from collections import Counter

data = [x.rstrip('\n').split(' -> ') for x in open('garrett\day5\d5-input.txt', 'r')]

points = []

for line in data:
    #gets the start and end values
    x1, y1 = list(map(int, (line[0].split(','))))
    x2, y2 = list(map(int, (line[1].split(','))))

    #stores the points of the horizontal and vertical lines in a list
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x, y))

    #stores the points of the diagonal lines in a list
    else:
        xinc = 1 if x1 < x2 else -1
        yinc = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + xinc, xinc):
            points.append((x, y))
            y += yinc
        
overlaps = len([pt for pt in Counter(points).values() if pt > 1])
print(overlaps)
