#gets only the character values after the delimiter
data = [x.split('|')[1].replace('\n', '').split() for x in open('garrett\day8\d8-input.txt', 'r')]

count = 0
for strings in data:
    for x in strings:
        length = len(x)
        if length < 5 or length == 7:
            count += 1

print(count)