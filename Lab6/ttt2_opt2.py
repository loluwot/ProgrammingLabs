'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random

#globals
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# pre_compute_rows = [2*3*5, 7*11*13, 17*19*23]
# pre_compute_columns = [2*7*17, 3*11*19, 5*13*23]
# pre_compute_diagonals = [2*11*23, 5*11*17]
# net_compute = pre_compute_rows + pre_compute_columns + pre_compute_diagonals
# prods = [1, 1]
row_count = [[0 for _ in range(2)] for __ in range(3)]
col_count = [[0 for _ in range(2)] for __ in range(3)]
diag_count = [[0 for _ in range(2)] for __ in range(2)]
moves = ['O', 'X']

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
    board[coord[0]][coord[1]] = mark
    update_count(coord[0], coord[1], mark)

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def get_free_squares(board):
    def helper(i):
        a, b = to_coord(i)
        return not (board[a][b] in ['O', 'X'])
    return list(map(to_coord, filter(helper, list(range(1, 10)))))

def update_count(rx, ry, mark):
    mi = moves.index(mark)
    row_count[rx][mi] += 1
    col_count[ry][mi] += 1
    if rx == ry:
        diag_count[0][mi] += 1
    if rx == 4 - ry:
        diag_count[1][mi] += 1

def make_random_move(board, mark):
    rx, ry = random.choice(get_free_squares(board))
    update_count(rx, ry, mark)
    board[rx][ry] = mark

def is_row_all_marks(board, row_i, mark):
    return all([v == mark for v in board[row_i]])

def is_column_all_marks(board, col_i, mark):
    return all([board[i][col_i] == mark for i in range(len(board))])

def is_win(board):
    for row in row_count:
        for i, x in enumerate(row):
            if x >= 3:
                return moves[i]
    for col in col_count:
        for i, x in enumerate(col):
            if x >= 3:
                return moves[i]
    for diag in diag_count:
        for i, x in enumerate(diag):
            if x >= 3:
                return moves[i]


if __name__ == '__main__':
    board = make_empty_board()
    
    # count = 0
    player_move = input('Select O or X as player mark: ')
    assert player_move in moves
    while True:
        print_board_and_legend(board)
        square = input(f'Input coordinates here: ')
        try:
            square = int(square)
        except:
            break
        put_in_board(board, player_move, square)
        # count += 1
        print_board_and_legend(board)
        print('Computer makes move.')
        make_random_move(board, moves[1 - moves.index(player_move)])
        win = is_win(board)
        if win:
            print(f'Winner is {win}.')
            break
    print('FINAL STATE')
    print(get_free_squares(board))
    print_board_and_legend(board)    
    print("\n\n")
    
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    
    # print_board_and_legend(board)            