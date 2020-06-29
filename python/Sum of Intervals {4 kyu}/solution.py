def sum_of_intervals(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(list(range(arr[i][0],arr[i][1])))
    arr = []
    for i in range(len(newArr)):
        for j in range(len(newArr[i])):
            arr.append(newArr[i][j])
    return len((set(arr)))