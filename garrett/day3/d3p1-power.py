  
f = open("garrett\day3\d3-input.txt", "r")

ones = [0] * 12 #empty list to store the amount of ones
values = 0      #keeps track of how many elements have been counted

#loops through the file until the end is reached
stillData = True
while stillData:
    data = f.readline()
    if data:
        #gets the data and converts the binary to an integer
        data = int(data, 2) 

        #incraments each bit in a list
        for i in range(len(ones)):
            ones[i] += bool(data & 2**(len(ones) - i - 1))
        
        #incraments vow many values have been read
        values += 1
    else:
        stillData = False
f.close()

gamma = 0
epsilon = 0
#gets the binary value of the average bits, calculates gammaing integer value, calculates compliment
for i in range(len(ones)):
    ones[i] = ones[i] // (values // 2)
    gamma += ones[i] * 2**(len(ones) - i - 1)
    epsilon += (1 - ones[i]) * 2**(len(ones) - i - 1)

print('number:     ', bin(gamma))
print('compliment: ', bin(epsilon))
print('multiplied value: ', gamma * epsilon)