import numpy as np
def print_matrix(M_lol):
    M = np.matrix(M_lol)
    print(M)

def get_lead_row(row):
    s = list(filter(lambda x: row[x] != 0, range(len(row))))
    return s[0] if len(s) != 0 else len(row)

def get_row_to_swap(M, start_i):
    s =list(filter(lambda x: get_lead_row(M[x]) < get_lead_row(M[start_i]) and x > start_i, sorted(range(len(M)), key=lambda x: get_lead_row(M[x]))))
    return -1 if len(s) == 0 else s[0]

def add_rows_coefs(r1, c1, r2, c2):
    return [r1[i]*c1 + r2[i]*c2 for i in range(len(r1))]

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        M[i] = add_rows_coefs(M[i], 1, M[row_to_sub], -M[i][best_lead_ind]/M[row_to_sub][best_lead_ind])

def forward_step(M):
    for ii in range(len(M) - 1):
        for i in range(len(M) - 1):
            j = get_row_to_swap(M, i)
            if j == -1:
                continue
            M[i], M[j] = M[j], M[i]
        eliminate(M, ii, get_lead_row(M[ii]))

def backward_step(M):
    # M = M[::-1]
    M.reverse()
    # print(M)
    for ii in range(len(M) - 1):
        eliminate(M, ii, get_lead_row(M[ii]))
        # print(M)
    M.reverse() 
    for i in range(len(M)):
        M[i] = add_rows_coefs(M[i], 0, M[i], 1/M[i][get_lead_row(M[i])])
    # print(M)

def solve(M, b):
    augmented = [M[i] + [b[i]] for i in range(len(M))]
    forward_step(augmented)
    backward_step(augmented)
    return [v[-1] for v in augmented] 

print_matrix([[1, 2], [3, 4]])
print(get_lead_row([0, 0, 0,0]))
M = [[5, 6, 7, 8],
[0, 0, 0, 1],   
[0, 0, 5, 2],
[0, 1, 0, 0]]
b = [2, 3, 4, 5]
sol = solve(M, b)
M = np.matrix(M)
b = np.matrix(b)
sol = np.matrix(sol)
sol = sol.transpose()
print(sol)
print(M*sol)
# eliminate(M, 1, 2)

# print(get_row_to_swap(M, 1))