import matplotlib.pyplot as plt
import numpy as np

positions = [p.split(',') for p in open('garrett\day7\d7-input.txt', 'r')]
positions = list(map(int, positions.pop(0)))

plt.hist(positions, bins=100)
plt.xlabel('Submarine Position')
plt.ylabel('Number of Ships')
plt.show()

def calcSeries(num):
    return sum([x for x in range(num + 1)])

#loops through each positon and checks if it will have the min fuel burn
biggest = max(positions)
finalPos = 0

#finds the position that has the smallest varriance
smallestVar = 89791190
for i in range(biggest):
    varriance = np.mean([abs(x - i)**2 for x in positions])
    if smallestVar > varriance: 
        smallestVar = varriance
        finalPos = i - 1
    
#calculates the fuel burn of the position
fuel = 0
for p in positions:
    fuel += calcSeries(abs(finalPos - p))           
print('fuel: %d  finalPos: %d' % (fuel, finalPos))

