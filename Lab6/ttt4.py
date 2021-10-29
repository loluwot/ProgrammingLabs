'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
import functools

#globals
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
prime_prod = functools.reduce(lambda x, y: x*y, primes)
pre_compute_rows = [2*3*5, 7*11*13, 17*19*23]
pre_compute_columns = [2*7*17, 3*11*19, 5*13*23]
pre_compute_diagonals = [2*11*23, 5*11*17]
net_compute = pre_compute_rows + pre_compute_columns + pre_compute_diagonals
moves = ['O', 'X']
prods = [1, 1]
AI_precompute = []


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    b = b % a
    return gcd(b, a)

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
def to_coord(square_num):
    return (square_num-1)//3, (square_num-1) % 3

def put_in_board(board, mark, square_num):
    coord = to_coord(square_num)
    if not board[coord[0]][coord[1]] in moves:
        prods[moves.index(mark)] *= primes[square_num-1]
        board[coord[0]][coord[1]] = mark
        return True
    return False

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def get_free_ns(board):
    def helper(i):
        a, b = to_coord(i)
        return not (board[a][b] in ['O', 'X'])
    return list(filter(helper, list(range(1, 10))))

def get_free_squares(board):
    return list(map(to_coord, get_free_ns(board)))

def make_random_move(board, mark):
    rx, ry = random.choice(get_free_squares(board))
    sq = rx*3 + ry
    prods[moves.index(mark)] *= primes[sq]
    board[rx][ry] = mark

def is_row_all_marks(board, row_i, mark):
    return all([v == mark for v in board[row_i]])

def is_column_all_marks(board, col_i, mark):
    return all([board[i][col_i] == mark for i in range(len(board))])

def win_prod(prod):
    for v in net_compute:
        for i in range(2):
            if prod[i] % v == 0:
                return moves[i]
    else:
        if prod[0]*prod[1] == prime_prod:
            return -1

def is_win():
    return win_prod(prods)

def win_next(board, mark):
    mi = moves.index(mark)
    for v in net_compute:
        potential = v/gcd(prods[mi], v)
        if potential in primes:
            idx = primes.index(potential)
            put_in_board(board, mark, idx + 1)
            break
    else:
        make_random_move(board, mark)

def eval(state, idx = False):
    free, prod, mi = state
    sign = (1 - 2*mi)

    win = win_prod(prod)
    if win:
        if win != -1:
            yield -sign
        else:
            yield 0

    states = []
    for i, f in enumerate(free):
        n_free = free[::]
        del n_free[i]
        n_prod = prod[::]
        n_prod[mi] *= primes[f-1]
        states.append((n_free, n_prod, (mi+1) % 2))
    # print(states)
    evals = [sign*next(eval(state1)) for state1 in states]

    yield sign*max(evals)
    if idx:
        yield free[max(list(range(len(states))), key=lambda x: evals[x])]

#State: (free, prod, mi)
def optimal_ai(board, mark):
    # if len(AI_precompute) == 0:
    mi = moves.index(mark)
    frees = get_free_ns(board)
    print(frees)
    score, idx = list(eval((frees, prods, mi), idx=True))
    print(idx)
    put_in_board(board, mark, idx)
    

if __name__ == '__main__':
    board = make_empty_board()
    while True:
        player_move = input('Select O or X as player mark: ')
        if player_move in moves:
            break
        print('Not O or X.')
    while True:
        print_board_and_legend(board)
        while True:
            square = input(f'Input coordinates here: (Input non-integer to exit)')
            try:
                square = int(square)
            except:
                break
            if put_in_board(board, player_move, square):
                break
            print('Spot already occupied.')
        print_board_and_legend(board)
        win = is_win()
        if win:
            if win != -1:
                print(f'Winner is {win}. ')
            else:
                print(f'Draw.')
            break
        print('Computer makes move.')
        optimal_ai(board, moves[1 - moves.index(player_move)])
        win = is_win()
        if win:
            print_board_and_legend(board)  
            if win != -1:
                print(f'Winner is {win}. ')
            else:
                print(f'Draw.')
            break
    print("\n\n")
    
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    
    # print_board_and_legend(board)            