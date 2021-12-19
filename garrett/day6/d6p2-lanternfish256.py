from collections import Counter

#gets the data
fishTimes = list(map(int, open('garrett\day6\d6-input.txt', 'r').readline().split(','))) 


timers = Counter({timer:0 for timer in range(10)}) #creates an empty counter object with all the times
fishes = Counter(fishTimes)                        #counts the fish times
fishes.update(timers)                              #updates with the empty values

for i in range(256):
    #creates more time eight fish and time six fish from the ones that are at zero
    fishes[7] += fishes.get(0, 0)
    fishes[9] += fishes.get(0, 0)

    #shifts the fish down a time
    fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}

#sums the fish
total = sum(fishes.values())
print('total fish:', total)