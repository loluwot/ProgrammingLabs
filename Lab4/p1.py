def count_evens(L):
    count = 0
    for elem in L:
        count += (elem + 1) % 2
    
    return count

# or 

def count_evens(L):
    return sum([(i+1) % 2 for i in L])