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
        #adds the read value to a list as a string
        s = str(read).replace('\n', '')
        data.append(s)
        
        #converts the binary to an integer
        read = int(read, 2) 
        
        #incraments each bit in a list
        for i in range(len(ones)):
            ones[i] += bool(read & 2**(len(ones) - i - 1))
        
        #incraments vow many values have been read
        values += 1
    else:
        stillLines = False

gamma = 0
epsilon = 0
#gets the binary value of the average bits, calculates gamma integer value, calculates compliment
for i in range(len(ones)):
    ones[i] = ones[i] // (values // 2)
    gamma += ones[i] * 2**(len(ones) - i - 1)
    epsilon += (1 - ones[i]) * 2**(len(ones) - i - 1)

data.sort(reverse=True)
print(data)

oxygen = 0
co2    = 0
print('o2: %d  co2: %d\nmultiplied: %d' % (oxygen, co2, oxygen * co2))