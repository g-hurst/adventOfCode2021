path = './AdventOfCodeDay2InputFile.txt'
fileID = open(path, 'r')
fileClean = [line.split(" ") for line in fileID.readlines()]
horizontal = 0
vertical = 0
product = 0

for lines in fileClean:
    if(lines[0] == 'forward'):
        horizontal += int(lines[1])
    elif(lines[0] == 'up'):
        vertical -= int(lines[1])
    elif(lines[0] == 'down'):
        vertical += int(lines[1])


product = horizontal * vertical
#print(fileClean)

print("Product: " + str(product))
print("Vertical: " + str(vertical))
print("Horizontal: " + str(horizontal))