'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random

#globals
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
    if not board[coord[0]][coord[1]] in moves:
        board[coord[0]][coord[1]] = mark
        return True
    return False
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

def make_random_move(board, mark):
    free = get_free_squares(board)
    if len(free) != 0:
        rx, ry = random.choice(get_free_squares(board))
        board[rx][ry] = mark

def is_row_all_marks(board, row_i, mark):
    return all([v == mark for v in board[row_i]])

def is_column_all_marks(board, col_i, mark):
    return all([board[i][col_i] == mark for i in range(len(board))])

if __name__ == '__main__':
    board = make_empty_board()
    
    # count = 0
    player_move = input('Select O or X as player mark: ')
    assert player_move in moves
    while True:
        print_board_and_legend(board)
        while True:
            square = input(f'Input coordinates here: ')
            try:
                square = int(square)
            except:
                break
            if put_in_board(board, player_move, square):
                break
            print('Spot already occupied.')
        # count += 1
        print_board_and_legend(board)
        print('Computer makes move.')
        make_random_move(board, moves[1 - moves.index(player_move)])
    print('FINAL STATE')
    print(get_free_squares(board))
    print_board_and_legend(board)    
    print("\n\n")
    
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    
    # print_board_and_legend(board)            