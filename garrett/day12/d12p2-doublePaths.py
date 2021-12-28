from collections import defaultdict, deque

#gets the input and returns data in a dict
def getInput(path):
    pairs =  [x.rstrip('\n').split('-') for x in open(path, 'r')]
    
    #turns the data into a dict
    d = defaultdict(list)
    for pair in pairs:
        d[pair[0]].append(pair[1])
        d[pair[1]].append(pair[0])

    return d

#counts the paths
def countpaths(map):
    ct = 0
    tracker = deque([('start', set(['start']), False)])
    
    while tracker:
        #removes the current step in the path
        p, seen, double = tracker.popleft()
        
        #only counts paths that hit the end point
        if p == "end":
            ct += 1
            continue
        
        for c in map[p]:
            if c not in seen:
                #assures small caves are not revisited
                seen_cp = set(seen)
                if c.islower(): seen_cp.add(c)
                
                #adds the next step of the path
                tracker.append((c, seen_cp, double))
            
            #accounts for if the lower case is visited a second time
            elif not double and c not in ['start', 'end']: tracker.append((c, seen, True))
    
    return ct
            
            
if __name__ == '__main__':
    testInput = getInput('garrett\day12\\p2-testinput.txt')
    mainInput = getInput('garrett\day12\d12-input.txt')

    assert countpaths(testInput) == 36

    pathCount = countpaths(mainInput)
    
    print('total paths is:', pathCount)