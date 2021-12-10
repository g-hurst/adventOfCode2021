#gets only the character values after the delimiter
dataRight = [x.split('|')[1].replace('\n', '').split() for x in open('garrett\day8\d8-input.txt', 'r')]
dataLeft = [x.split('|')[0].replace('\n', '').split() for x in open('garrett\day8\d8-input.txt', 'r')]

#returns the amount of characters from s1 that are in s2
def checkInside(s1, s2):
    count = 0
    for c in s1:
        if c in s2: count += 1
    return count 

#returns true if s1 is in s2
def contains(s1, s2):
    if checkInside(s1, s2) == len(s1): return True
    else: return False        

def getKey(myDict, n):
    items = myDict.items()
    for key,value in items:
        if len(value) == len(n) and checkInside(n, value) == len(n):
            return key
    #return 0

total = 0
for i in range(len(dataLeft)):
    #empty dict to store ssd values
    ssd = {0:'\0', 1: '\0', 2: '\0', 3: '\0', 4: '\0', 5: '\0', 6: '\0', 7: '\0', 8: '\0', 9: '\0'}

    #fill the dictionary witht the corosponding character combinations
    for digit in dataLeft[i]:
        length = len(digit)
        if   length == 2: ssd[1] = digit
        elif length == 3: ssd[7] = digit
        elif length == 4: ssd[4] = digit
        elif length == 7: ssd[8] = digit
    for digit in dataLeft[i]:
        length = len(digit)
        if length == 5: #either 2, 3, or 5
            if contains(ssd[1], digit) or contains(ssd[7], digit):                    ssd[3] = digit
            elif checkInside(ssd[1], digit) == 1 and checkInside(ssd[4], digit) == 2: ssd[2] = digit
            else: ssd[5] = digit 

        elif length == 6: #either 0, 6, or 9
            if (contains(ssd[4], digit) or contains(ssd[3], digit)):                 ssd[9] = digit
            elif checkInside(ssd[1], digit) == 1 or checkInside(ssd[7], digit) == 2: ssd[6] = digit
            else:                                                                    ssd[0] = digit

    #sum the numbers
    keyArr = [getKey(ssd, digit) for digit in dataRight[i]]
    num = int(''.join(map(str, keyArr)))
    total += num

    # print(ssd)
    # print(dataRight[i])
    # print(keyArr)
    # print(num)

print('sum: ', total)

