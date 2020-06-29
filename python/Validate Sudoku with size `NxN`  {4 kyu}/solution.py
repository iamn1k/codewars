class Sudoku(object):
    def __init__(self, board):
        self.board = board
    def is_valid(self):
        import math
        print('board:',self.board)
        temp = []    
        # valid - these are numbers that can be found in the sudoku grid
        valid = [i for i in range(1,len(self.board)+1) ]
        # check - check grid on valid with use sum valid
        check = sum(valid)
        # border - matrix squareness check
        border = int(len(self.board)**0.5)
        # horizontal scanning of matrix and adding it to temp array

        #   <-->
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                temp.append(self.board[i][j])
        #   <-->

        # emergency check

        #   <-->
        if len(temp) == 1 and isinstance(temp[0],bool):
            return False
        #   <-->

        # Is the matrix square?

        # <-->
        if math.sqrt(len(temp)).is_integer() == False:
            return False
        # <-->

        else: 
            temp =[]

        # horizontal sudoku grid check

        # <-->
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] in valid:
                    temp.append(self.board[i][j])
            if (0 in temp) or (int(sum(temp)) != check):
                return False
                break
            else:
                temp = []
        # <-->

        # vertical sudoku grid check
        # <-->
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[j][i] in valid:
                    temp.append(self.board[j][i])
            if (0 in temp) or (int(sum(temp)) !=  check):
                return False
                break
            else:
                temp = []
        # <--> 

        #check for squares with side NxN, where N is the square root of border length
        # <-->
        temp = []
        temp = [[x for r in self.board[i:i+border] for x in r[j:j+border]] for j in range(0,len(self.board),border) for i in range(0,len(self.board),border)]
        for i in range(len(temp)):
            if sum(temp[i]) != check:
                return False
                break
        # <-->

        # If all checks pass, I return True
        return True