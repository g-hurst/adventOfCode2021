
#gets the data from the text file
with open("garrett\d1p1-input.txt", "r") as f:
    data = f.readlines()

#cleans data
for x in range(len(data)):
    data[x] = int(data[x])
    
#checks for increases
increases = 0
for x in range(len(data) - 1):
    if data[x] < data[x + 1]:
        increases += 1
    #print("%d   %d" % (data[x], increases))

print(increases)