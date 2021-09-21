def mult_M_v(M, v):
    ans_v = []
    for i in range(len(v)):
        # s = 0
        # for ii, m in enumerate(M[i]):
        #     s += m*v[ii]

        s = sum([M[i][ii]*v[ii] for ii in range(len(M[i]))])
        
        ans_v.append(s)

    return ans_v

M = [[1,2],[3,4],[5,6]]
v = [1,3]

print(mult_M_v(M, v))