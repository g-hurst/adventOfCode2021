path = './AdventOfCodeDay1InputFile.txt'
fileID = open(path, 'r')
fileClean = [int(line) for line in fileID]
sumOne = fileClean[0] + fileClean[1] + fileClean[2]
sumTwo = 0
increases = 0

for i in range(len(fileClean) - 3):
    sumTwo = sumOne - fileClean[i] + fileClean[i + 3]
    if(sumTwo > sumOne):
        increases += 1
    sumOne = sumTwo

print(increases)




