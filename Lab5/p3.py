def repeats(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True
    return False