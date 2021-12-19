#gets the data
data = [x.rstrip('\n') for x in open('garrett\day10\d10-input.txt', 'r')]

#defines chunk openers and closers
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

#goes through each line
illegalChars = []
for line in data:    
    stack = []
    
    #cycles through each char of the chunk
    for c in line:
        #adds an opening bracket to the stack
        if c in pairs:
            stack.append(c)
        
        #removes opening bracket from the stack if the closing matches. Else, appends illegal char
        else:
            if pairs[stack[-1]] == c: stack.pop(-1)
            else: 
                illegalChars.append(c)
                break
    
#gets the total syntax score
pointVals = {')':3, ']':57, '}':1197, '>':25137}
points = 0
for c in illegalChars:
    points += pointVals[c]

print(f'total points is {points}')