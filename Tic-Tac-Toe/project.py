def sum(a, b, c ):
    return a + b + c

#Function for displaying the board
def PrintBoard(xState, oState):
    #Code to set the state of position
    zero = 'X' if xState[0] else ('O' if oState[0] else ' ')
    one = 'X' if xState[1] else ('O' if oState[1] else ' ')
    two = 'X' if xState[2] else ('O' if oState[2] else ' ')
    three = 'X' if xState[3] else ('O' if oState[3] else ' ')
    four = 'X' if xState[4] else ('O' if oState[4] else ' ')
    five = 'X' if xState[5] else ('O' if oState[5] else ' ')
    six = 'X' if xState[6] else ('O' if oState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if oState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if oState[8] else ' ')
    #Code to print the  board
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")

#Function to check if a player have won
def WinCheck(xState,oState):
    '''List of all possible winning combinations, where each sublist contains indices 
    that correspond to positions on the tic-tac-toe board'''
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
            if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
                print("Player 1(X) has won the match!!")
                return 1
            if(sum(oState[win[0]], oState[win[1]], oState[win[2]]) == 3):
                print("Player 2(O) has won the match!!")
                return 0
    return -1

# Function to check if the game is a draw
def DrawCheck(xState, oState):
    if all(xState[i] == 1 or oState[i] == 1 for i in range(9)):
        return True
    return False

#Main body
xState = [0,0,0,0,0,0,0,0,0]
oState = [0,0,0,0,0,0,0,0,0]
PlayerTurn = 1  #1 for X & 0 for O
print('Welcome to the game of TIC TAC TOE')
print('Positions are as follows:')
print(' 0 | 1 | 2 ')
print('---|---|---')
print(' 3 | 4 | 5 ')
print('---|---|---')
print(' 6 | 7 | 8 ')
print(" ")

while(True):
    PrintBoard(xState,oState)
    if(PlayerTurn==1):
        print("Player 1's(X) turn")
        print(" ")
    else:
        print("Player 2's()) turn")
        print(" ")

    # Get valid position
    while True:
        position = int(input("Please enter the position you want (0-8): "))
        print(" ")
        if position < 0 or position > 8:
            print("Invalid position try again ://")
            print(" ")
        elif xState[position] == 1 or oState[position] == 1:
            print("Position is already taken pls try again :/")
            print(" ")
        else:
            break

    if(PlayerTurn == 1):
        xState[position] = 1
    else:
        oState[position] = 1

    # Check for a win after every move
    cwin = WinCheck(xState, oState)
    if(cwin != -1):
        PrintBoard(xState, oState)
        print("Match over!")
        break
    
    # Check for a draw
    if DrawCheck(xState, oState):
        PrintBoard(xState, oState)
        print("It's a draw!")
        break

    PlayerTurn = 1 - PlayerTurn