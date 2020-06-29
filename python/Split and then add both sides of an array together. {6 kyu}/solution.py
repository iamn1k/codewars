def split_and_add(Arr, n):
    if (len(Arr)<2):
       return list(Arr)
    i =0
    while (i <n):
        if len(Arr) % 2==0:
            curr = int(len(Arr) / 2)
            newArr = []
            for j in range(len(Arr)-curr):
                newArr.append(Arr[j] + Arr[j+curr])
            Arr = newArr
        elif len(Arr) % 2 !=0:
            curr = int((len(Arr) +1)/2)
            half1 = Arr[0:curr-1]
            half2 = Arr[curr-1:len(Arr)]
            newArr = [half2[0]]
            del half2[0]
            for j in range(curr -1):
                newArr.append(half1[j] + half2[j])
            Arr = newArr
        i += 1
    return Arr 
    