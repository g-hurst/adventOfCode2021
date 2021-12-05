import numpy as np
from copy import copy

class board():
    def __init__(self, data):
        self.nums = data  #sets the arr in paramter to data (must be 5x5)
        self.calledSpaces = np.zeros((5,5)) #creates an empty 5x5 array to store which positions have been called

    #returns 1 if the board has bingo
    def hasBingo(self):
        for i in range(5):
            #checks rows for bingo
            count = 0
            for j in range(5):
                count += self.calledSpaces[i][j]
            if count == 5: return 1
            
            count = 0
            #checks columns for bingo
            for j in range(5):
                count += self.calledSpaces[j][i]
            if count == 5: return 1
        return 0
    
    #updates 
    def markSquare(self, val):
        for i in range(5):
            for j in range(5):
                if self.nums[i][j] == val: self.calledSpaces[i][j] = 1
            
#gets the data from the file
with open('garrett\day4\d4p1-input.txt', 'r') as f:
    numbers = f.readline()
    boardData = f.readlines()

#creates an array of board objects that store the board
boards = []
for i in range(1, len(boardData), 6):
    boardNums = []
    for j in range(5):
        row = list(map(int, boardData[i + j].split()))
        boardNums.append(row)
    boards.append(board(boardNums))

#gets the first board that recieves bingo
bingoBoard = None
lastCalled = None
breakVal = False
numbers = list(map(int, numbers.split(',')))
for num in numbers:
    for i in range(len(boards)):
        boards[i].markSquare(num)
        if boards[i].hasBingo() == 1:
            bingoBoard = boards[i]
            lastCalled = num
            breakVal = True
            break
    if breakVal: break

#calculates the bingo sum
bingoSum = 0
breakVal = False
for i in range(5):
    for j in range(5):
        if bingoBoard.calledSpaces[i][j] == 0: 
            bingoSum += bingoBoard.nums[i][j]
    if breakVal: break


print("num: %d   sum: %d   mult: %d" % (num, bingoSum, num * bingoSum))
print(bingoBoard.nums)
print(bingoBoard.calledSpaces)