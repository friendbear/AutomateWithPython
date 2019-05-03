
# Input Key and Display Char
the_board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def print_board(board):
    print(board)


# Game Logic
turn = 'X'
while True:
    print_board(the_board)
    print('Next turn: ' + turn)
    move = input()
    if move not in the_board.keys():
        print('Illgal Input')
        continue
    else:
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


# full version
# https://github.com/oreilly-japan/automatestuff-ja/fullTicTacToe2.py
