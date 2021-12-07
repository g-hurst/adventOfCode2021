with open('garrett\day6\d6-input.txt', 'r') as f:
    data = f.readline()

fishTimes = list(map(int, data.split(',')))

#cycles through 80 days and updates fish accordingly
for i in range(80):
    #print('day: %d   fish: %d' % (i, len(fishTimes)))
    for j in range(len(fishTimes)):
        if (fishTimes[j] == 0):
            fishTimes[j] = 6
            fishTimes.append(8)
        else:
            fishTimes[j] -= 1

print(len(fishTimes))
