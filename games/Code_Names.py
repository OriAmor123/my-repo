import random

NAMES = list({'שחור', 'קשת', 'רחבה', 'זווית', 'ניילון', 'קרח', 'מפל', 'לשון', 'כוס', 'מיתר', 'קרן', 'יהלום', 'ציפורן', 'תבלין', 'אבקה', 'ינשוף', 'עוגה',
    'אפל', 'שיחה', 'לכלוך', 'שבר', 'מקרה', 'ריצה', 'פאזל', 'תקרה', 'סיר', 'יפה', 'מפית', 'פיה', 'קרש', 'טבעת', 'שמפו', 'גרב', 'צומת', 'ריקוד',
    'מסע', 'חרב', 'תיקון', 'דת', 'הר געש', 'קבר', 'שמן', 'צמר', 'חצי',  'גדר', 'צל', 'קצב',
})
NUM_OF_COLORS = {
    'red  ':8,
    'blue ':8,
    'black':1,
    'green':7
}
names_for_a_game = random.sample(NAMES, 25)
LEN_OF_WORDS = 6
# *Decide whether red or blue starts
PLAYERS = ['red  ', 'blue ']

starter = random.choice(PLAYERS)


round = 1
recent_starter_guess = 0
recent_second_guess = 0
recent_starter_definition = None
recent_second_definition = None
starter_correct_guesses = 0
second_correct_guesses = 0

# * Second_player
def second(first):
    PLAYERS.remove(first)
    return PLAYERS[0]
second_player = second(starter)

# *Aligning the words to the same length
def aligning_words(list_of_words):
    list_of_words = list_of_words.copy()
    for word in list_of_words:
        if len(word) < LEN_OF_WORDS:
            difference = LEN_OF_WORDS - len(word)
            aligned_word = word + ' ' * difference
            list_of_words[list_of_words.index(word)] = aligned_word
    return list_of_words
    
def print_agents_board(colors, starter):
    # *Creating a list with the colors
    colors[starter] = 9
    list_of_colors = []
    for color, times_appear in colors.items():
        for _ in range(times_appear):
            list_of_colors.append(color)

    # *Creating 2D table of the board in a list
    board = [[],[],[],[],[]]
    for row in range(5):
        for _ in range(5):
            color = random.choice(list_of_colors)
            board[row].append(color)
            list_of_colors.remove(color)
    # *Printing the actual board
    for row in range(5):
        for column in range(5):
            print(board[row][column], end='')
            if column < 4:
                print(' | ', end='')
        print()
        if row <4:
            print('--------------------------------------')
    return board

def create_2d_board(word_list):
    word_list = word_list.copy()
    board = [[],[],[],[],[]]
    # *Creating a list with 5 rows with 5 words each
    #appending a row 5 times
    for i in range(5):
        #creating the row
        for _ in range(5):
            word = word_list.pop()
            board[i].append(word[::-1])
    return board

def print_players_board(board):
    # * Creating the actual board
    #printing each row seperately
    for i in range(5):
        #passing through the row
        for j in range(5):
            print(f'{board[i][j]}', end='')
            #slicing with | only between 2 words
            if j < 4:
                print(' | ', end='')
            #moving to the next line
        print()
        if i <4:
            print('-------------------------------------------')

def starter_round(starter, word_list, color_table, board_table, aligned_board_table):
    global recent_starter_guess
    global recent_starter_definition
    global starter_correct_guesses
    global second_correct_guesses
    #* If there was a recent definition available, the colsole will print the definition
    if recent_starter_definition != None:
        print(f'Your recent definition was \"{recent_starter_definition}\", you have an additional 1 guess in this round.')
    starter_agents_definition = input(f'{starter} agents turn. Write a definition and a number of geusses: ')
    num_of_guesses = int(starter_agents_definition.split()[1])

    while num_of_guesses + recent_starter_guess > 0:
        # TODO: guessing words and one step back memory
        #checking if the word is in the board
        while True:
            current_guess = input(f'{starter} Players, you have {num_of_guesses + recent_starter_guess} guesses, write a guess: ')
            if current_guess in word_list:
                break
            else:
                print('The word isn\'t on the board, try again.')
        #getting the word's position & color
        for row in board_table:
            for word_in_row in row:
                if current_guess == word_in_row[::-1]:
                    current_guess_position = [board_table.index(row), row.index(word_in_row)]
                    break

        current_guess_row, current_guess_col = current_guess_position
        current_guess_color = color_table[current_guess_row][current_guess_col]
        
        #* determing whether the guess is red, green. blue, or black
        #if it is the correct one
        if current_guess_color == starter:
            aligned_board_table[current_guess_row][current_guess_col] = starter + ' '
            print(f'Correct! You have {num_of_guesses-1} guesses left.')
            print_players_board(aligned_board_table)
            
            starter_correct_guesses += 1
            recent_starter_guess = 0
            recent_starter_definition = None
            #* If the starter player won
            if starter_correct_guesses == 9:
                return 'won'

        elif current_guess_color == second_player:
            aligned_board_table[current_guess_row][current_guess_col] = second_player + ' '
            print(f'Wrong! A {second_player} word!')
            print_players_board(aligned_board_table)

            second_correct_guesses +=1
            recent_starter_guess = 1
            recent_starter_definition = starter_agents_definition.split()[0]
            if second_correct_guesses == 8:
                return 'lost'
            break

        elif current_guess_color == 'green':
            aligned_board_table[current_guess_row][current_guess_col] = 'green '
            print('Wrong! A green word!')
            print_players_board(aligned_board_table)

            recent_starter_guess = 1
            recent_starter_definition = starter_agents_definition.split()[0]
            break

        elif current_guess_color == 'black':
            print('You\'ve hit the asassin! You lost!')
            return 'lost'

def second_player_round(second, word_list, color_table, board_table, aligned_board_table):
    global recent_second_guess
    global recent_second_definition
    global second_correct_guesses
    global starter_correct_guesses
    #* If there was a recent definition available, the colsole will print the definition
    if recent_second_definition != None:
        print(f'Your recent definition was \"{recent_second_definition}\", you have an additional 1 guess in this round.')
    second_agents_definition = input(f'{second} agents turn. Write a definition and a number of geusses: ')
    num_of_guesses = int(second_agents_definition.split()[1])

    while num_of_guesses + recent_second_guess > 0:
        #checking if the word is in the board
        while True:
            current_guess = input(f'{second} Players, you have {num_of_guesses + recent_second_guess} guesses, write a guess: ')
            if current_guess in word_list:
                break
            else:
                print('The word isn\'t on the board, try again.')
        #getting the word's position & color
        for row in board_table:
            for word_in_row in row:
                if current_guess == word_in_row[::-1]:
                    current_guess_position = [board_table.index(row), row.index(word_in_row)]
                    break

        current_guess_row, current_guess_col = current_guess_position
        current_guess_color = color_table[current_guess_row][current_guess_col]
        
        #* determing whether the guess is red, green. blue, or black
        #if it is the correct one
        if current_guess_color == second_player:
            aligned_board_table[current_guess_row][current_guess_col] = second + ' '
            print(f'Correct! You have {num_of_guesses-1} guesses left.')
            print_players_board(aligned_board_table)
            
            second_correct_guesses += 1
            recent_second_guess = 0
            recent_second_definition = None
            #* If the starter player won
            if second_correct_guesses == 8:
                return 'won'

        elif current_guess_color == starter:
            aligned_board_table[current_guess_row][current_guess_col] = starter + ' '
            print(f'Wrong! A {starter} word!')
            print_players_board(aligned_board_table)

            starter_correct_guesses +=1
            recent_second_guess = 1
            recent_second_definition = second_agents_definition.split()[0]
            if starter_correct_guesses == 9:
                return 'lost'
            break

        elif current_guess_color == 'green':
            aligned_board_table[current_guess_row][current_guess_col] = 'green '
            print('Wrong! A green word!')
            print_players_board(aligned_board_table)

            recent_second_guess = 1
            recent_second_definition = second_agents_definition.split()[0]
            break

        elif current_guess_color == 'black':
            print('You\'ve hit the asassin! You lost!')
            return 'lost'

def main():
    color_table = print_agents_board(NUM_OF_COLORS, starter)
    print()
    board_table = create_2d_board(names_for_a_game) #a table for the visual board
    aligned_board_table = create_2d_board(aligning_words(names_for_a_game)) #the list of the aligned words
    print_players_board(aligned_board_table)
    winner = None

    # *Rounds
    global round
    while round:
        if round %2 !=0:
            round_result = starter_round(starter, names_for_a_game, color_table, board_table, aligned_board_table)
            if round_result == 'won':
                print(f'Congatulations! {starter} team won!')
                winner = starter
                break
            elif round_result == 'lost':
                print(f'{second_player} team won!')
                winner = second_player
                break
                
        else:
            round_result = second_player_round(second_player, names_for_a_game, color_table, board_table, aligned_board_table)
            if round_result == 'won':
                print(f'Congatulations! {second_player} team won!')
                winner = second_player
                break
            elif round_result == 'lost':
                print(f'{starter} team won!')
                winner = starter
                break
        round+=1
    
    print(f'Game Over!\nThanks For Playing!\n Team {winner} is the winner of the game')
# TODO: Making the ligic of the game, rounds, agents definition, one turn back memory, choosing words and marking them, winning/losing


if __name__ == '__main__':
    main()