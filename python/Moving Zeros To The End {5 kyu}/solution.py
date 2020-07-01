def move_zeros(arr):
    newArr = []
    zeros = []
    
    for i in range(len(arr)):
        if arr[i] == 0 or arr[i] == 0.0:
            if type(arr[i]) == int or type(arr[i]) == float:
                zeros.append(arr[i])
            else: 
                newArr.append(arr[i])
        else:
            newArr.append(arr[i])
    return newArr + zeros