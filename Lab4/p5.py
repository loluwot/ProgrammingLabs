import math
def pi_approx(N):
    s = 0
    for i in range(N):
        s += (-1)**i/(2*i+1)
    return s*4


def N_for_pi(digits):
    N = 0
    while (True):
        print(int(math.pi*(10**digits)) - int(pi_approx(N)*(10**digits)))
        if (int(math.pi*(10**digits)) - int(pi_approx(N)*(10**digits)) == 0):
            return N
        N += 1

print(N_for_pi(3))