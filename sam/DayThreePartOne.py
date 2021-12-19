path = './AdventOfCodeDay3Input.txt'
fileID = open(path, 'r')
fileClean = [line.strip('\n') for line in fileID.readlines()]
gammaRate = []
epsilonRate = []
zeroCount = 0
oneCount = 0
gammaDecimal = 0
epsilonDecimal = 0
i = 0
j = 0

while i < len(fileClean[0]):
    zeroCount = 0
    oneCount = 0
    while j < len(fileClean):
        if(fileClean[j][i] == '0'):
            zeroCount += 1
        elif(fileClean[j][i] == '1'):
            oneCount += 1
        j += 1
    j = 0
    if(zeroCount > oneCount):
        gammaRate.insert(i, '0')
    else:
        gammaRate.insert(i, '1')
    i += 1
    
i = 0

while i < len(gammaRate):
    if(gammaRate[i] == '0'):
        epsilonRate.insert(i, '1')
    else:
        epsilonRate.insert(i, '0')
    i += 1

i = 0

while i < len(gammaRate):
    if(gammaRate[i] == '1'):
        gammaDecimal += pow(2, len(gammaRate) - 1 - i)
    if(epsilonRate[i] == '1'):
        epsilonDecimal += pow(2, len(gammaRate) - 1 - i)
    i += 1

print(gammaDecimal * epsilonDecimal)
