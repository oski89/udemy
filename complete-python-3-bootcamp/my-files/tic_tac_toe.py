board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board_i = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Strings needed for printing the board
l_v = '   |   |   \n'
l_h = '-----------\n'
l_p = ' {0} | {1} | {2} \n'


def display_board(board):
    # A function that prints the game board
    l_v = '   |   |   \n'
    l_h = '-----------\n'
    l_p = ' {0} | {1} | {2} \n'

    print(
        l_v + l_p.format(board[7], board[8], board[9]) + l_v + l_h +
        l_v + l_p.format(board[4], board[5], board[6]) + l_v + l_h +
        l_v + l_p.format(board[1], board[2], board[3]) + l_v)


def player_input():
    player1 = ''

    # Keep asking Player 1 to choose a marker (X or O)
    while not (player1 == 'X' or player1 == 'O'):
        marker = input('Player 1, choose a marker (X or O): ')
        player1 = marker.upper()

        if player1 == 'X':
            print('Player 1 is X. Player 2 is O.')
            return('X', 'O')
        elif player1 == 'O':
            print('Player 1 is O. Player 2 is X.')
            return('O', 'X')
        else:
            print(f'{marker} is not a valid marker.')


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark)
    )


display_board(board_i)

player1_marker, player2_marker = player_input()

pos = int(input('Where do you want to play? (1-9) '))
place_marker(board, player1_marker, pos)
display_board(board)
win_check(board)
