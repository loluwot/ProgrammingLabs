import math
def pi_approx(N):
    s = 0
    for i in range(N):
        s += (-1)**i/(2*i+1)
    return s*4


def N_for_pi(digits):
    N = 0
    cur_approx = 0
    while (True):
        if (int(math.pi*(10**(digits - 1))) - int(cur_approx*4*(10**(digits- 1))) == 0):
            return N
        cur_approx += (-1)**N/(2*N + 1)
        N += 1

print(N_for_pi(2))