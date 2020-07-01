def fib(n):
    arr = [1,1]
    for i in range(2,n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr
def perimeter(n):
    return 4 * sum(fib(n))    