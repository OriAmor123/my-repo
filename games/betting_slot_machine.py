import random

MAX_LINES = 3
ROWS, COLS = 3, 3
MIN_BET = 1
MAX_BET = 200

SYMBOL_COUNT = {
    'A': 2,
    'B': 3,
    'C': 5,
    'D': 7
}
SYMBOL_VALUE = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def deposit():
    while True:
        current_deposit = input('How much money would you like to deposit? $')
        if current_deposit.isdigit():
            return int(current_deposit)
        else:
            print('this value isn\'t valid, enter a valid amount of money.')

def lines_to_bet():
    while True:
        lines = input('How many lines would you like to bet on (max 3 lines)? ')
        if lines.isnumeric():
            if 1 <= int(lines) <= MAX_LINES:
                return int(lines)
            else:
                print(f'How can bet on max {MAX_LINES} lines.')
        else:
            print('invalid amount of lines!')

def money_to_bet():
    while True:
        current_bet = input('How much money would you like to bet for each line: ')
        if current_bet.isnumeric():
            if MIN_BET <= int(current_bet) <= MAX_BET:
                return int(current_bet)
            else:
                print(f'Your bet must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('This number isn\'t valid.')

def spin_slot(rows, cols, symbols):
    #adding the symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #creating the board
    board = []
    for _ in range(cols):
        board.append(random.sample(all_symbols, rows))
    return board

#printing the board
def print_board(board):
    for row in range(len(board[0])): #for each row
        for column in board:
            if board.index(column) == len(board)-1:
                print(column[row]) #print the whole row
            else:
                print(column[row], end=' | ') #print the whole row
        if row < len(board[0])-1:
            print('----------')

#checks if the player won
def if_the_player_won(board):
    rows_played = len(board[0]) #number of rows in the board
    values_which_won = [] #a list of the symbols which the player got a full line of them
    for row in range(rows_played):
        row_check = [] #checking each row seperately
        for col_in_row in board:
            row_check.append(col_in_row[row]) #creating the row
        #checking the current row
        for value in row_check: 
            if value != row_check[0]: #if one symbol is diff, skips to the next row
                break
        else:
            values_which_won.append(board[0][row]) #if they're the same, adds the value to the list
    return values_which_won

def adding_money_to_balance(bet_on_each_line, lines_to_bet, value_win_list, symbol_values):
    total_win = 0
    if len(value_win_list)>0: #only if he won something
        for value in value_win_list:
            if lines_to_bet >0: #ensure the player wins doesn't win more that the lines he bet on
                row_win = symbol_values[value] * bet_on_each_line
                total_win+=row_win
                lines_to_bet-= 1 #for the ensurance too
            else:
                break
    return total_win

#round of spinning
def spin_machine(balance):
    #amount of lines to bet
    lines = lines_to_bet()
    #amount of money to bet
    while True:
        money = money_to_bet()
        if money*lines > balance:
            print('Your bet is bigger than your balance.')
        else:
            break
    print(f'You\'re betting on ${money} for {lines} lines, your total bet is {money*lines}')
    balance -=money*lines
    #spinning the wheel
    current_board = spin_slot(ROWS, COLS, SYMBOL_COUNT)
    #printing the wheel
    print_board(current_board)
    #checking if the player won
    values_of_win = if_the_player_won(current_board)
    #adding the prize to the balance
    total_win = adding_money_to_balance(money, lines, values_of_win, SYMBOL_VALUE)
    print(f'You won ${total_win}')
    balance+=total_win  
    return balance

def main():
    running = True
    balance = deposit()
    while running and balance >0:
        print(f'Your balance is ${balance}')
        play = input('Press enter to play (q to quit) ').lower()
        if play == 'q':
            running = False
            continue
        elif play == '':
            balance = spin_machine(balance)
    print('Game Over!\nThanks For Playing')


if __name__ == '__main__':
    main()