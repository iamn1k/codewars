def valid_solution(board):
    import numpy as np
    temp = []
    valid = [i for i in range(1,10)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in valid:
                temp.append(board[i][j])
        if (0 in temp) or (int(sum(temp)) != 45):
            return False
            break
        else:
            temp = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] in valid:
                temp.append(board[j][i])
        if (0 in temp) or (int(sum(temp)) != 45):
            return False
            break
        else:
            temp = []
    temp = []
    temp = [[x for r in board[i:i+3] for x in r[j:j+3]] for j in range(0,9,3) for i in range(0,9,3)]
    for i in range(len(temp)):
        if sum(temp[i]) != 45:
            return False
            break
    return True
            