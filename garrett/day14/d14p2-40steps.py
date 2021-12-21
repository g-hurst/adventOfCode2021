from collections import Counter

#gets the data
with open('garrett\day14\d14-input.txt', 'r') as f:
    template = f.readline().rstrip('\n')
    f.readline() #skips the blank line
    
    #dict from the pairs and associated vals
    rules = {}
    for x in f.readlines():
        rules[x.split(' -> ')[0]] = x.split(' -> ')[1].rstrip('\n')

#counts the total pairs of the polymer
chunks = [template[i] + template[i+1] for i in range(len(template) - 1)]
pairs = Counter(chunks)
for _ in range(40):
    newPairs = Counter()
    for chunk in pairs:
        newPairs[chunk[0] + rules[chunk]] += pairs[chunk]
        newPairs[rules[chunk] + chunk[1]] += pairs[chunk]
    pairs = newPairs

#counts the added letters
letters = Counter()
for chunk in pairs:
    letters[chunk[0]] += pairs[chunk]
#adds the last character
letters[chunks[-1][-1]] += 1

#gets the max and min values
minimum = min(letters, key=letters.get)
maximum = max(letters, key=letters.get)

print('most common minus least common:', letters[maximum] - letters[minimum])
