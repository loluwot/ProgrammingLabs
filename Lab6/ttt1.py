'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


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

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
    
if __name__ == '__main__':
    board = make_empty_board()
    moves = ['O', 'X']
    count = 0
    while True:
        print_board_and_legend(board)
        square = input(f'Input coordinates here (current move is {moves[count%2]}): ')
        try:
            square = int(square)
        except:
            break
        put_in_board(board, moves[count%2], square)
        count += 1
    print('FINAL STATE')
    print_board_and_legend(board)    
    print("\n\n")
    
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    
    # print_board_and_legend(board)            