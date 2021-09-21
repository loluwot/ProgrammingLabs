
def cube_sum(n):
    return sum([i**3 for i in range(1, n+1)])

def check_sum(n):
    return (n*(n+1)/2)**2

def check_sum_up_to_n(N):
    for i in range(1, N+1):
        if cube_sum(i) != check_sum(i):
            return False
    return True

print(check_sum_up_to_n(100))