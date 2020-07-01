def valid_parentheses(str):
    str = list(str)
    dif = 0
    for i in range(len(str)):
        if dif < 0:
            return False
            break
        if str[i] == '(':
            dif += 1
        elif str[i] == ')':
            dif -= 1  
    if dif == 0:
        return True
    else:
        return False
            