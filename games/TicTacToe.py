BOARD = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
PLAYERS_SYMBOL = ['X','Y'] #player 1 is X, player 2 is Y
PREVIOUS_SPOTS = []
available_spots = [1,2,3,4,5,6,7,8,9]

#printing the screen (adaptive to changes)
def print_screen(board):
    for i in range(3):
        for j in range(3):
            if j==2:
                print(board[i][j])
            else:
                print(board[i][j], end=' | ')
        if i <2:
            print('---------')

#checks if someone win
def check_who_win(board):
    for i in range(3):
        #checks rows
        if board[i][0]==board[i][1]==board[i][2] !=' ':
            winner = board[i][0]
            return winner
        #checks columns
        elif board[0][i]==board[1][i]==board[2][i] !=' ':
            winner = board[0][i]
            return winner
    if board[0][0]==board[1][1]==board[2][2] !=' ':
        winner = board[0][0]
        return winner
    elif board[0][2]==board[1][1]==board[2][0] !=' ':
        winner = board[0][2]
        return winner
    else:
        return None

#checks if the spot is valid and in the domain
def is_valid_choice(spot):
    if spot.isnumeric():
        if 1<=int(spot)<=9:
            return True
        else:
            return False
    else:
        return False

#checks if the spot is free or already used
def check_spot_if_was_already(spot, recent_spots):
    if spot in recent_spots:
        return False
    else:
        recent_spots.append(spot)
        return True


#assigning the choice on the board
def assign_symbol(board, symbol, spot, recent_spots):
    spot= int(spot)
    recent_spots.remove(spot)
    if spot == 7:
        board[0][0] = symbol
    elif spot == 8:
        board[0][1] = symbol
    elif spot == 9:
        board[0][2] = symbol
    elif spot == 4:
        board[1][0] = symbol
    elif spot == 5:
        board[1][1] = symbol
    elif spot == 6:
        board[1][2] = symbol
    elif spot == 1:
        board[2][0] = symbol
    elif spot == 2:
        board[2][1] = symbol
    elif spot == 3:
        board[2][2] = symbol

def main():
    print_screen(BOARD)
    
    current_turn=1
    while current_turn <=9:
        if current_turn % 2 !=0: #Player 1 turn, symbol X
            current_spot = input(f'{PLAYERS_SYMBOL[0]} turn!\ncount starts from top left, and moving right, in each column, choose a spot using a number between 1-9: ')
            while True:
                #ensures the spot is valid
                if not is_valid_choice(current_spot):
                    current_spot = input('invalid spot, choose a spot using a number between 1-9: ')
                    continue
                #ensures the spot is available
                if not check_spot_if_was_already(current_spot, PREVIOUS_SPOTS):
                    print(f'Available spots: {available_spots}')
                    current_spot = input('Already taken spot, choose a different spot using a number between 1-9:')
                    continue
                #if the spot is good, adding the spot to the board and printing the board
                assign_symbol(BOARD, PLAYERS_SYMBOL[0], current_spot, available_spots)
                print_screen(BOARD)
                break
            if check_who_win(BOARD) == PLAYERS_SYMBOL[0]:
                break
#-----------------------------------------------------------------------------------
        else: #Player 2 turn, symbol Y
            current_spot = input(f'{PLAYERS_SYMBOL[1]} turn!\ncount starts from top left, and moving right, in each column, choose a spot using a number between 1-9: ')
            while True:
                #ensures the spot is valid
                if not is_valid_choice(current_spot):
                    current_spot = input('invalid spot, choose a spot using a number between 1-9: ')
                    continue
                #ensures the spot is available
                if not check_spot_if_was_already(current_spot, PREVIOUS_SPOTS):
                    print(f'Available spots: {available_spots}')
                    current_spot = input('Already taken spot, choose a different spot using a number between 1-9:')
                    continue
                #if the spot is good, adding the spot to the board and printing the board
                assign_symbol(BOARD, PLAYERS_SYMBOL[1], current_spot, available_spots)
                print_screen(BOARD)
                break
            if check_who_win(BOARD) == PLAYERS_SYMBOL[1]:
                break
        current_turn+=1
    
    #end of the game
    print('Game over!')
    if check_who_win(BOARD)== None:
        print('Draw')
    else:
        print(f'The winner is {check_who_win(BOARD)}')

if __name__ == '__main__':
    main()