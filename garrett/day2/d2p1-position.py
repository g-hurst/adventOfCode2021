with open("garrett\day2\d2p1-input.txt", "r") as f:
    data = f.readlines()


pos = 0
depth = 0
for x in range(len(data)):
    #cleaning data
    data[x]    = data[x].split(' ')
    data[x][1] = int(data[x][1])

    #get add final depth and position
    if 'f' in data[x][0]:   pos += data[x][1]
    elif 'd' in data[x][0]: depth += data[x][1]
    else:                   depth -= data[x][1]

print("position: %d\ndepth: %d\nmultiplied: %d" % (pos, depth, pos * depth))

