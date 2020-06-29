def uniq(Arr): 
    if len(Arr)<2:
        return Arr
    else:
        dubl = [Arr[0]]
        for i in range(len(Arr)-1):
            if Arr[i] != Arr[i+1]:
                dubl.append(Arr[i+1])
        return dubl