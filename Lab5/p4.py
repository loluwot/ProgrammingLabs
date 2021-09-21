def print_matrix_dim(M):
    print(f'{len(M)}x{len(M[0])}')

print_matrix_dim([[1,2],[3,4],[5,6]])

def mult_M_v(M, v):
    ans_v = []
    for i in range(len(v)):
        s = sum([M[i][ii]*v[ii] for ii in range(len(M[i]))])
        ans_v.append(s)

    return ans_v

M = [[1,2],[3,4],[5,6]]
v = [1,3]

print(mult_M_v(M, v))

def mult_MM(M1, M2):
    M = [[0 for i in range(len(M2[0]))] for ii in range(len(M1))]
    for c in range(len(M2[0])):
        cc = [M2[ii][c] for ii in range(len(M2))]
        cnew = mult_M_v(M1, cc)
        for ii in range(len(M)):
            M[ii][c] = cnew[ii]
    return M

M1 = [[1,0], [1,1]]
M2 = [[1,1], [2,3]]

print(mult_MM(M1, M2))