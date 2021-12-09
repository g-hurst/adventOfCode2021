#gets only the character values after the delimiter
data = [x.split('|')[1].replace('\n', '').split() for x in open('garrett\day8\d8-input.txt', 'r')]

