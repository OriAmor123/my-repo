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
            word = random.choice(word_list)
            board[i].append(word[::-1])
            word_list.remove(word)
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

def starter_round(starter, word_list, color_table, board_table):
    starter_agents_definition = input(f'{starter} agents turn. Write a definition and a number of geusses: ')
    global recent_starter_guess
    current_definition = starter_agents_definition.split()[0]
    num_of_guesses = int(starter_agents_definition.split()[1])

    while num_of_guesses > 0:
        # TODO: guessing words and one step back memory
        #checking if the word is in the board
        while True:
            current_guess = input(f'{starter} Players, write a guess: ')
            if current_guess in word_list:
                break
            else:
                print('The word isn\'t on the board, try again.')
        #getting the word's position & color
        for row in board_table:
            for word_in_row in row:
                if current_guess == word_in_row[::-1]:
                    current_guess_position = [board_table.index(row), row.index(word_in_row)]
                    break # TODO: The code doesn't find the current guess in the board list
            else:
                break
        current_guess_row, current_guess_col = current_guess_position
        current_guess_color = color_table[current_guess_row][current_guess_col]

        #* determing whether the guess is red, green. blue, or black
        #if it is the correct one
        if current_guess_color == starter:
            board_table[current_guess_row][current_guess_col] = starter + ' '
            print(f'Correct! You have {num_of_guesses-1} guesses left.')
        # elif current_guess_color == second_player:

        


def second_player_round(second):
    pass

def main():
    color_table = print_agents_board(NUM_OF_COLORS, starter)
    print()
    board_table = create_2d_board(names_for_a_game) #a table for the visual board
    aligned_board_table = create_2d_board(aligning_words(names_for_a_game)) #the list of the aligned words
    print_players_board(aligned_board_table)
    # TODO: The word list and the board ard NOT THE SAME

    # *Rounds
    global round
    while round:
        if round %2 !=0:
            starter_round(starter, names_for_a_game, color_table, board_table)
        else:
            second_player_round(second_player)
        round+=1
# TODO: Making the ligic of the game, rounds, agents definition, one turn back memory, choosing words and marking them, winning/losing


if __name__ == '__main__':
    main()