import copy

f = open("garrett\day3\d3p1-input.txt", "r")

data = []
ones = [0] * 12 #empty list to store the amount of ones
values = 0      #keeps track of how many elements have been counted

#loops through the file until the end is reached
stillLines = True
while stillLines:
    read = f.readline()
    if read:

        #adds the read value to a list
        data.append(int(read, 2))
        
        #converts the binary to an integer
        read = int(read, 2) 
        
        #incraments each bit in a list
        for i in range(len(ones)):
            ones[i] += bool(read & 2**(len(ones) - i - 1))
        
        #incraments vow many values have been read
        values += 1
    else:
        stillLines = False
f.close()

gamma = 0
epsilon = 0

#gets the binary value of the average bits, calculates gamma integer value, calculates compliment
for i in range(len(ones)):
    ones[i] = ones[i] // (values // 2)
    gamma += ones[i] * 2**(len(ones) - i - 1)
    epsilon += (1 - ones[i]) * 2**(len(ones) - i - 1)

def removeElements(val, arr, bit):
    #gets desired bit of the value to compare to
    currentBit = val[len(val) - bit]

    #removes the elements from the array that do not contain the desired bit in the desired location
    arr = [x for x in arr if ((x // 2**(bit - 1) ) % 2) == currentBit]

    #recursive case
    if len(arr) > 1 and bit > 0:
        arr = removeElements(val, arr, bit - 1)

    return arr

oxygen = removeElements(ones, data, 12)[0]
print(ones)
for i in range(len(ones)):
    ones[i] = 1 - ones[i]
print(ones)
co2    = removeElements(ones, data, 12)[0]
print("g: %d   e: %d\nmultiplied: %d" % (gamma, epsilon, gamma * epsilon))
print('o2: %d  co2: %d\nmultiplied: %d' % (oxygen, co2, oxygen * co2))