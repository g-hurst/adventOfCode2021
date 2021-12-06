"""
Advent of Code 2021: Day 1 - Part 1
Ron Bejerano
12/03/2021
"""

#opens text file and sets data to variable fid
fid = open("C:/Users/Ron/OneDrive/Documents/2021 Advent of Code/day1_input.txt", "r")

#creates an integer list given the data from the text file using the map function
measurements = list(map(int, fid.readlines()))
#variable to count the number of times the depth increased
count = 0

#for loop to run through all the iterations in the list
for n in range(0, len(measurements) - 3):
    #creates window comparisons and resets after every iteration
    window1 = measurements[n] + measurements[n + 1] + measurements[n + 2]
    window2 = measurements[n + 1] + measurements[n + 2] + measurements[n + 3]
    #compares one data point to the data point directly succeeding it
    if window1 < window2:
        #if true, count increases by 1
        count += 1
    #loop control variable
    n += 1

#message output
print(count)