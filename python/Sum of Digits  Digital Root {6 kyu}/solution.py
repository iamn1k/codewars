def f(n):
    return sum(map(lambda x: int(x),list(str(n))))
def digital_root(n):
    while True:
        if len(str(f(n))) > 1:
            n = f(n)
        else:
            n = f(n)
            return n
            