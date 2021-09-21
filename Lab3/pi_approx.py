def pi_approx(N):
    s = 0
    for i in range(N):
        s += (-1)**i/(2*i+1)
    return s*4



print(pi_approx(1000))