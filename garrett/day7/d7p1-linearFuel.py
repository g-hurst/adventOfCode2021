positions = [p.split(',') for p in open('garrett\day7\d7-input.txt', 'r')]
positions = list(map(int, positions.pop(0)))

#loops through each positon and checks if it will have the min fuel burn
biggest = max(positions)
minFuel = 350000
finalPos = 0
for i in range(biggest):
    fuel = 0
    for p in positions:
        fuel += abs(i - p)
    if fuel < minFuel: 
        minFuel = fuel
        finalPos = i
                 
print('fuel: %d  finalPos: %d' % (minFuel, finalPos))