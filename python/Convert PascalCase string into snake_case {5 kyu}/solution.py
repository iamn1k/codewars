def to_underscore(string):    
    print(string)
    if len(str(string)) == 1:
        return str(string)
    string = list(string)
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for i in range(len(string)):
        if string[i] not in big:
            res += string[i]
        else:
            res += '_' + string[i]
    return (res.lower())[1:]