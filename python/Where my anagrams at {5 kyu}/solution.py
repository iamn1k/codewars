def anagrams(inp,lists):
    inp = list(inp)
    inp.sort()
    index =[]
    result=[]
    _lists = []
    copy = lists
    for i in range(len(lists)):
        a = list(lists[i])
        (a).sort()
        _lists.append(a)
    for i in range(len(lists)):
        if inp == _lists[i]:
            index.append(i)
    for i in range(len(index)):
        result.append(copy[index[i]])
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    return result