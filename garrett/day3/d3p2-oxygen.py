data = [x.rstrip('\n') for x in open("garrett\day3\d3-input.txt", "r")]

oxygen = data
co2 = data
for i in range(len(data[0])):
    #calculates the oxygen rating
    if len(oxygen) > 1:
        mostCommon = sum([int(num[i]) for num in oxygen]) // (len(oxygen) / 2)
        oxygen = [x for x in oxygen if int(x[i]) == mostCommon]

    #calculates the co2 rating
    if len(co2) > 1:
        mostCommon = not bool(sum([int(num[i]) for num in co2]) // (len(co2) / 2))
        co2 = [x for x in co2 if int(x[i]) == mostCommon]

#converts the binary to integers
oxygen, co2 = int(oxygen[0], 2), int(co2[0], 2)

print('o2: %d  co2: %d\nmultiplied: %d' % (oxygen, co2, oxygen * co2))