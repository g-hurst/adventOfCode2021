path = './AdventOfCodeDay3Input.txt'
fileID = open(path, 'r')
fileClean = [line.strip('\n') for line in fileID.readlines()]
oxygenList = fileClean
carbonList = fileClean

for i in range(len(fileClean[0])):

    if(len(oxygenList) > 1):
        common = sum([int(x[i]) for x in oxygenList]) // (len(oxygenList) / 2)
        oxygenList = [x for x in oxygenList if int(x[i]) == common]

    if(len(carbonList) > 1):
        common = sum([int(x[i]) for x in carbonList]) // (len(carbonList) / 2)
        carbonList = [x for x in carbonList if int(x[i]) != common]

oxygenList = int(oxygenList[0], 2)
carbonList = int(carbonList[0], 2)

print(oxygenList * carbonList)