
fid = open("C:/Users/Ron/OneDrive/Documents/2021 Advent of Code/day3_input.txt")

report = list(map(int, fid.readlines()))

gamma = 0
epsilon = 0

for j in range(12):
    zero_count = 0
    one_count = 0
    for i in range(len(report)):
        if int(report[i] / 10**(11-j)) % 2 == 0:
            zero_count += 1
        else:
            one_count += 1
    if (zero_count > one_count):
        gamma += 0 * 10**(11-j)
        epsilon += 1 * 10**(11-j)
    else:
        gamma += 1 * 10**(11-j)
        epsilon += 0 * 10**(11-j)

power_gamma = int(str(gamma), 2)
power_epsilon = int(str(epsilon), 2)

print(power_gamma * power_epsilon)
