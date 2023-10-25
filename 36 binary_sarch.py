def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1