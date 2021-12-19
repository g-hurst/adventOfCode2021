with open("C:/Users/Ron/OneDrive/Documents/2021 Advent of Code/day3_input.txt", "r") as fid:
    report = fid.readlines()
    report2 = report.copy()
    report.sort()
    report2.sort()

oxygen = ''
carbon = ''

for i in range(12):
    zeroes = 0
    ones = 0
    flag = 0
    for j in range(len(report)):
        if report[j][i] == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        for k in range(len(report)):
            if report[k][i] == '0':
                flag += 1
        oxygen += '0'
        del report[flag:]
    elif ones > zeroes:
        for l in range(len(report)):
            if report[l][i] == '1':
                flag += 1
        oxygen += '1'
        del report[:flag - 1]
    else:
        for m in range(len(report)):
            if report[m][i] == '1':
                flag += 1
        oxygen += '1'
        del report[:flag - 1]

for a in range(12):
    zeroes = 0
    ones = 0
    flag = 0
    for b in range(len(report2)):
        if report2[b][a] == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        for c in range(len(report2)):
            if report2[c][a] == '1':
                flag += 1
        carbon += '1'
        del report2[:flag - 1]
    elif ones > zeroes:
        for d in range(len(report2)):
            if report2[d][a] == '0':
                flag += 1
        carbon += '0'
        del report2[flag:]
    else:
        for e in range(len(report2)):
            if report2[e][a] == '0':
                flag += 1
        carbon += '0'
        del report2[flag:]

print(oxygen)
print(carbon)

generator = int(oxygen, 2)
scrubber = int(carbon, 2)

print(generator)
print(scrubber)

print(generator * scrubber)