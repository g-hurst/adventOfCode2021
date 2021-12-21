from collections import Counter

#gets the data
with open('garrett\day14\d14-input.txt', 'r') as f:
    polymer = [x for x in f.readline().rstrip('\n')]
    f.readline() #skips the blank line
    
    #dict from the pairs and associated vals
    pairs = {}
    for x in f.readlines():
        pairs[x.split(' -> ')[0]] = x.split(' -> ')[1].rstrip('\n')

for _ in range(10):
    stack = []
    for element in polymer:
        if len(stack) == 0: stack.append(element)
        else: 
            curr = stack[-1] + element
            stack.append(pairs[curr])
            stack.append(element)

    polymer = stack
 
count = Counter(polymer)
minimum = min(count, key=count.get)
maximum = max(count, key=count.get)

print('most common minus least common:', count[maximum] - count[minimum])