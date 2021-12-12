with open('garrett\day6\d6-input.txt', 'r') as f:
    data = f.readline()

fishTimes = list(map(int, data.split(',')))

#calculates the amount of fish produced from a single fish after a given number of days
def calcSeries(start, stop):
    times = [start]
    for i in range(stop):
        print('day', i, 'fish', len(times))
        for j in range(len(times)):
            if (times[j] == 0):
                times[j] = 6
                times.append(8)
            else:
                times[j] -= 1
        
    return len(times)

def calcFish(startTime, stop):
    fish = 0
    stop -= startTime + 1

    if stop >= 0:
        if fish > 1:
            fish += 1
            fish += calcFish(8, stop)
            fish += calcFish(6, stop)
        else:
            fish += 1
            fish += calcFish(8, stop)
            fish += calcFish(6, stop)

    return fish

#stores the amount of fish produced for for each start time
n = 80
times = []
for t in range(1, 6):
    print('calculating start time ', t)
    times.append(calcFish(t, n))
    print(times[t - 1])

#calculates the total number of fish
fishCount = 0
for f in fishTimes:
    fishCount += times[f - 1]

print(fishCount)
