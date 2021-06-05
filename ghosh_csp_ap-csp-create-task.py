import random # for computer to choose spots on the board randomly
import sys # for exiting game with messages

# Collection type to use on the rubric Row 2
# This is a dictionary so the value pairs can be updated
# based on the key values, which will match user inputs
# CREATE TASK LIST/OTHER COLLECTION TYPE
ttt_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

# list that will contain the eligible choices for computer to pick from
# starts with complete gameboard (since it's empty), and elements are slowly removed
computer_choices = ['1','2','3','4','5','6','7','8','9']

# create board based off the above map and format tictactoe style
def createBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# this function will randomly place the computer's choices and allow
# user input with the variable move
# CREATE TASK FUNCTION WITH 1 OR MORE PARAMETERS
def place_counter(turn,available_computer_slots):
    count = 0
    for i in range(10):
        # if it's the human's turn
        if turn == 'X':
            print("It's your turn Player to move X. Enter placement: ")
            move = input()
            # this checks if the position on the board is empty
            # this is why the map is necassary, as it allows the program
            # to easily check if it's empty

            # if user's number choice (which is used as the key pair here)
            # leads to an empty position on the map, then this is an eligible move
            if ttt_board[move] == ' ': 
                ttt_board[move] = turn
                # make this the official user turn since it's allowed

                # this is for making sure the computer randomly chooses from an open spot
                # now since the user has taken this spot, it's removed from the choice of open spots
                available_computer_slots.remove(move)
                createBoard(ttt_board)
                # increment variable increased for once (this is used to check for ties later on)
                count += 1

                # start checking for wins
                if ttt_board['7'] == ttt_board['8'] == ttt_board['9'] != ' ': # top row
                    createBoard(ttt_board)                
                    sys.exit("Game Over\n ---- " +turn + " won. ----")
                elif ttt_board['4'] == ttt_board['5'] == ttt_board['6'] != ' ': # middle row
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----")
                elif ttt_board['1'] == ttt_board['2'] == ttt_board['3'] != ' ': # bottom row
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----")
                elif ttt_board['1'] == ttt_board['4'] == ttt_board['7'] != ' ': # left column
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----")
                elif ttt_board['2'] == ttt_board['5'] == ttt_board['8'] != ' ': # middle column
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----")
                elif ttt_board['3'] == ttt_board['6'] == ttt_board['9'] != ' ': # right column
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----") 
                elif ttt_board['7'] == ttt_board['5'] == ttt_board['3'] != ' ': # positive diagonal
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----")
                elif ttt_board['1'] == ttt_board['5'] == ttt_board['9'] != ' ': # negative diagonal
                    createBoard(ttt_board)
                    sys.exit("Game Over\n ---- " +turn + " won. ----") 

                # full board with all 9 (thus count == 9) is a tie (all the above options weren't true)
                elif count == 9:
                    sys.exit("Game Over - Tied")

            # if nothing works, then it must already be filled
            # such that it didn't fit the other if statements
            else:
                print("Space is occupied.\nEnter placement:")
                
            
        elif turn == 'O':
            print('It\'s my turn, the Computer, to move O. My placement:')
            move = random.choice(available_computer_slots)
            available_computer_slots.remove(move)
            ttt_board[move] = turn
            createBoard(ttt_board)


            if ttt_board['7'] == ttt_board['8'] == ttt_board['9'] != ' ': # top row
                createBoard(ttt_board)                
                sys.exit("Game Over\n ---- " +turn + " won. ----")
            elif ttt_board['4'] == ttt_board['5'] == ttt_board['6'] != ' ': # middle row
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----")
            elif ttt_board['1'] == ttt_board['2'] == ttt_board['3'] != ' ': # bottom row
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----")
            elif ttt_board['1'] == ttt_board['4'] == ttt_board['7'] != ' ': # left column
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----")
            elif ttt_board['2'] == ttt_board['5'] == ttt_board['8'] != ' ': # middle column
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----")
            elif ttt_board['3'] == ttt_board['6'] == ttt_board['9'] != ' ': # right column
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----") 
            elif ttt_board['7'] == ttt_board['5'] == ttt_board['3'] != ' ': # positive diagonal
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----")
            elif ttt_board['1'] == ttt_board['5'] == ttt_board['9'] != ' ': # negative diagonal
                createBoard(ttt_board)
                sys.exit("Game Over\n ---- " +turn + " won. ----") 

            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            elif count == 9:
                sys.exit("Game Over - Tied")


        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O' # player => computer
        else:
            turn = 'X' # computer => player
    
# initilize empty board
print('''Welcome to a game of tic-tac-toe!
Here's what a blank board looks like: 
''')

# first call to show user game board
createBoard(ttt_board)
print('''To play, here are the counter placements.
7|8|9
-+-+-
4|5|6
-+-+-
1|2|3
Now good luck against the computer!

Clearing game board....
Cleared.''')


######################### Initialization complete #########################
turn = 'X'
game = True
while game == True:
    createBoard(ttt_board)
    count = 0
    
    if turn == 'X': # Player's turn
        place_counter('X',computer_choices)
        turn = 'O'
    elif turn == 'O': # Computer's turn
        place_counter('O',computer_choices)
        turn = 'X'

