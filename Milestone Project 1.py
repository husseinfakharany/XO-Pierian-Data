#MILESTONE PROJECT 1

def display_board(board):
    print("{}|{}|{}".format(board[1], board[2], board[3]))
    print("-|-|-")
    print("{}|{}|{}".format(board[4], board[5], board[6]))
    print("-|-|-")
    print("{}|{}|{}".format(board[7], board[8], board[9]))

def player_input(current):
    print("{} choose your marker (X or O): ".format(current))
    plyinp = input()
    while (plyinp != 'X' and plyinp != 'O'):
        print("{} choose your marker (X or O): ".format(current))
        plyinp = input()
    return plyinp

def place_marker(board, marker, position):
    board.pop(position)
    board.insert(position, marker)

def win_check(board, mark):
    # Horizantal Win
    for i in [1, 4, 7]:
        if board[i] == board[i + 1] and board[i] == board[i + 2] and board[i] == mark:
            return True
    # Vertical Win
    for i in [1, 2, 3]:
        if board[i] == board[i + 3] and board[i] == board[i + 6] and board[i] == mark:
            return True

    # Diagonal Win
    if board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True

    if board[3] == board[5] and board[3] == board[7] and board[3] == mark:
        return True

    else:
        return False

import random


def choose_first():
    num = random.randint(1, 2)
    return num


def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in board:
        if i == ' ':
            return False

    return True

def player_choice(board):
    pos = int(input("Choose a position: \n"))
    while space_check(board, pos) != True:
        print("Ths position has already been taken")
        pos = int(input("Choose a position: \n"))
    return pos

def replay():
    choice = input("Do you want to play again? (Y,N)")
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False
    else:
        replay()

print('Welcome to Tic Tac Toe!')
name1 = input("Player 1's name: \n")
name2 = input("Player 2's name: \n")
while name2 == name1:
    print("Choose a different name than {}".format(name1))
    name2 = input("Player 2's name: \n")
players = {name1: 1, name2: 2}
points = {name1: 0, name2: 0}
rep = True
while rep == True:
    first = choose_first()
    if players[name1] == first:
        firstplayer = name1
        secondplayer = name2
    elif players[name2] == first:
        firstplayer = name2
        secondplayer = name1
    # Board Init
    board = ['#']
    for i in range(1, 10):
        board.insert(i, ' ')
    print("The game has chosen {} to start".format(firstplayer))
    markerone = player_input(firstplayer)
    print("{} has chosen {}".format(firstplayer, markerone))
    if markerone == 'O':
        markertwo = 'X'
    elif markerone == 'X':
        markertwo = 'O'
    markerplayer = {firstplayer: markerone, secondplayer: markertwo}
    print("{} has been assigned to {}".format(markertwo, secondplayer))
    i = 1
    e = 1
    j = 0
    while not (full_board_check(board)):
        if j == 0:
            print("Round {}".format(i))
            display_board(board)
            currentmarker = markerplayer[firstplayer]
            currentplayer = firstplayer
            j = 1
        elif j == 1:
            currentmarker = markerplayer[secondplayer]
            currentplayer = secondplayer
            j = 0
        print("{}'s turn".format(currentplayer))
        pos = player_choice(board)
        place_marker(board, currentmarker, pos)
        display_board(board)
        if win_check(board, currentmarker) == True:
            if currentplayer == name1:
                points[name1] = + 1
            elif currentplayer == name2:
                points[name2] = +1
            print("{} has won!".format(currentplayer))
            print(points)
            break
        if e % 2 == 0:
            i += 1
        e += 1
    if replay() == True:
        rep = True
    else:
        rep = False
print("The game has ended\n")
print(points)