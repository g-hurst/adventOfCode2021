#gets the data from the text file
with open("garrett\day1\d1p1-input.txt", "r") as f:
    data = f.readlines()

#cleans data
for x in range(len(data)):
    data[x] = int(data[x])
    

increases = 0
s1 = data[0] + data[1] + data[2] #initial sum

for x in range(len(data) - 3):
    s2 = s1 - data[x] + data[x + 3]
    
    #compares with three measurement system
    if s1 < s2:
        increases += 1

    print("%d   %d   %d" % (s1, s2, increases))
    s1 = s2 #transfers the second sum to the first sum varriable

    

print(increases)