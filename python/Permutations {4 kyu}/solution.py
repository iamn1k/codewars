def permutations(string):
    import itertools
    return list(set([''.join(el) for el in itertools.permutations(list(string))]))