def narcissistic(n):
    global i
    num = list(map(lambda x:int(x),list(str(n))))
    numCheck = n
    i = 1
    while True:
        _num = list(map(lambda x:int(x**i),num))
        if sum(_num)== numCheck:
            return True
            break
        else:
            i += 1
        if sum(_num) > numCheck*2:
            return False
            break