def solution(arr):
    if len(arr) < 3:
        return arr
    res = []
    temp =[]
    if arr[0]+1 == arr[1]:
        temp.append(arr[0])
    else:
        a = [arr[0]]
        res.append(a)
    for i in range(2,len(arr)):
        if arr[i-1]+1 == arr[i]:
            temp.append(arr[i-1])
        else:
             temp.append(arr[i-1])
             res.append(temp)
             temp = []
    if arr[-2]+1 == arr[-1] and temp != []:
        temp.append(arr[-1])
    else:
        a = [arr[-1]]
        res.append(a)
    res.append(temp)
    result = ''
    for i in range(len(res)):
        if len(res[i]) == 1:
            result = result + str(res[i][0]) + ','
        elif len(res[i]) == 2:
            result = result + str(res[i][0]) + ',' + str(res[i][1]) + ','
        elif len(res[i]) > 2:
            result = result + str(res[i][0]) + '-' + str(res[i][-1]) + ','
    if result[-1] == ',':
        return result[:-1]
    return result