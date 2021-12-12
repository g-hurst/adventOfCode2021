
fid = open("C:/Users/Ron/OneDrive/Documents/2021 Advent of Code/day2_input.txt", "r")

directions = fid.readlines()

horizontal = 0
depth = 0
aim = 0

for i in range(len(directions)):
    movement = directions[i].split()
    if movement[0] == "forward":
        horizontal += int(movement[1])
        depth += aim * int(movement[1])
    elif movement[0] == "down":
        aim += int(movement[1])
    elif movement[0] == "up":
        aim -= int(movement[1])

print(horizontal * depth)