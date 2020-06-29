def snail(arr):
    temp_list = []
    if arr and len(arr) > 1:
        if isinstance(arr[0], list):
            temp_list.extend(arr[0])
        else:
            temp_list.append(arr[0])
        arr.pop(0)
        for lis_index in range(len(arr)):
            temp_list.append(arr[lis_index][-1])
            arr[lis_index].pop(-1)
        if isinstance(arr[-1], list):
            temp_list.extend(arr[-1][::-1])
        else:
            temp_list.append(arr[-1])
        arr.pop(-1)
        for lis_index in range(len(arr)):
            temp_list.append(arr[::-1][lis_index][0])
            arr[::-1][lis_index].pop(0)
        temp_list.extend(snail(arr))
        return temp_list
    elif arr:
        return arr[0]
    else:
        return []