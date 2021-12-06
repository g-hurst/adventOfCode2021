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

def getWorst(boards, nums, i):
    num = nums[i]
    #marks the boards with the called number
    for j in range(len(boards)):
        boards[j].markSquare(num)

    #removes the boards that already have bingo
    boards = [x for x in boards if x.hasBingo() == 0]
    
    #recursive case
    if len(boards) > 1: boards = getWorst(boards, nums, i + 1)

    return boards

#finds the worst board
numbers = list(map(int, numbers.split(',')))
bingoBoard = getWorst(boards, numbers, 0)[0]

#calculates when the board will win
num = 0
for n in numbers:
    bingoBoard.markSquare(n)
    if bingoBoard.hasBingo() == 1: 
        num = n
        break

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