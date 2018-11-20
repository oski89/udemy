from __future__ import print_function
import random

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

    while not (player1 == 'X' or player1 == 'O'):
        marker = input('Player 1, choose a marker (X or O): ')
        player1 = marker.upper()

        if player1 == 'X':
            print('Player 1 is X. Player 2 is O.')
            return ('X', 'O')
        elif player1 == 'O':
            print('Player 1 is O. Player 2 is X.')
            return ('O', 'X')
        else:
            print('{} is not a valid marker.'.format(marker))


def place_marker(board, marker, position):
    board[position] = marker
    return board


def is_win(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or # horizontal top
        (board[4] == board[5] == board[6] == mark) or # horizontal middle
        (board[1] == board[2] == board[3] == mark) or # horizontal bottom
        (board[7] == board[4] == board[1] == mark) or # vertical left
        (board[8] == board[5] == board[2] == mark) or # vertical middle
        (board[9] == board[6] == board[3] == mark) or # vertical right
        (board[7] == board[5] == board[3] == mark) or # diagnoal from top left
        (board[1] == board[5] == board[9] == mark)) # diagnoal from bottom left


def choose_first():
    flip = random.randint(1, 2)
    return 'Player {}'.format(flip)


def is_not_occupied(board, position):
    return board[position] == ' '


def is_tie(board):
    return board.count(' ') == 0


def player_choice(board):
    pos = 0
    while pos not in range(1, 10) or is_not_occupied(board, pos):
        pos = int(input('Where do you want to play? (1-9) '))
    return pos


def is_replay():
    answer_u = ''
    while not (answer_u == 'Y' or answer_u == 'N'):
        answer = input('Would you like to play again? (Y or N) ')
        answer_u = answer.upper()
        if answer_u == 'Y':
            return True
        elif answer_u == 'N':
            return False
        else:
            print('{} is not a valid answer.'.format(answer))


# WHILE LOOP TO KEEP PLAYING THE GAME
print('Welcome to Tic Tac Toe!')

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X, O)

    the_board = ['#'] + [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' goes first...')

    play_game_u = ''

    while not (play_game_u == 'Y' or play_game_u == 'N'):
        play_game = input('Ready to play? (Y or N) ')
        play_game_u = play_game.upper()

        if play_game_u == 'Y':
            game_on == True
        elif play_game_u == 'N':
            game_on == False
        else:
            print('{} is not a valid answer.'.format(play_game))

        ## GAME PLAY

        while game_on:

            ## PLAYER ONE TURN
            if turn == 'Player 1':

                # Display the board
                display_board(the_board)

                # Choose a position
                position = player_choice(the_board)

                # Place the marker at the position
                place_marker(the_board, player1_marker, position)

                # Check if they won
                if is_win(the_board, player1_marker):
                    display_board(the_board)
                    print('Player 1 has won!')
                    game_on = False

                # Check if tie
                else:
                    if is_tie(the_board):
                        display_board(the_board)
                        print('It\'s a tie!')
                        game_on = False

                    # No win and no tie -> next players turn
                    else:
                        turn = 'Player 2'

            ## PLAYER TWO TURN
            if turn == 'Player 2':

                # Display the board
                display_board(the_board)

                # Choose a position
                position = player_choice(the_board)

                # Place the marker at the position
                place_marker(the_board, player2_marker, position)

                # Check if they won
                if is_win(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False

                # Check if tie
                else:
                    if is_tie(the_board):
                        display_board(the_board)
                        print('It\'s a tie!')
                        game_on = False

                    # No win and no tie -> next players turn
                    else:
                        turn = 'Player 1'

    # BREAK OUT OF THE WHILE LOOP ON is_replay() == False
    if not is_replay():
        break

