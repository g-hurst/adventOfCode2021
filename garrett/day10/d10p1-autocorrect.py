import numpy as np

#gets the data
data = [x.rstrip('\n') for x in open('garrett\day10\d10-input.txt', 'r')]

#defines chunk openers and closers
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

#goes through each line
corruptedChunks = []
finalStacks = []

for i in range(len(data)):    
    line = data[i]
    stack = []
    
    #cycles through each char of the chunk
    for c in line:
        #adds an opening bracket to the stack
        if c in pairs:
            stack.append(c)
        
        #removes opening bracket from the stack if the closing matches. Else, appends index of corrupted chunk
        else:
            if pairs[stack[-1]] == c: stack.pop(-1)
            else: 
                corruptedChunks.append(i)
                break
    
    #adds the final stack to a list
    finalStacks.append(stack)
   
#removes the corrupted stacks
finalStacks = [x for x in finalStacks if finalStacks.index(x) not in corruptedChunks]

#gets the total autocomplete score
pointVals = {'(':1, '[':2, '{':3, '<':4}
points = []
for line in finalStacks:
    sum = 0
    for i in range(len(line) - 1, -1, -1):
        sum *= 5
        sum += pointVals[line[i]]
    points.append(sum)

middle = int(np.median(points))

print(f'total points is {middle}')