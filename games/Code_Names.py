import random

NAMES = list({'שחור', 'קשת', 'רחבה', 'זווית', 'ניילון', 'קרח', 'מפל', 'לשון', 'כוס', 'מיתר', 'קרן', 'יהלום', 'ציפורן', 'תבלין', 'אבקה', 'ינשוף', 'עוגה',
    'אפל', 'שיחה', 'לכלוך', 'שבר', 'מקרה', 'ריצה', 'פאזל', 'תקרה', 'סיר', 'יפה', 'מפית', 'פיה', 'קרש', 'טבעת', 'שמפו', 'גרב', 'צומת', 'ריקוד',
    'מסע', 'חרב', 'תיקון', 'דת', 'הר געש', 'קבר', 'שמן', 'צמר', 'חצי',  'גדר', 'צל', 'קצב',
})
NUM_OF_COLORS = {
    'red':8,
    'blue':8,
    'black':1,
    'green':7
}
names_for_a_game = random.sample(NAMES, 25)
LEN_OF_WORDS = 6
# *Decide whether red or blue starts
PLAYERS = ['red', 'blue']
starter = random.choice(PLAYERS)

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
    board = [[],[],[],[],[]]
    # TODO: 1. adding the colors in the board list
    # TODO: 2. creating the board


def print_players_board(names):
    names = names.copy()
    board = [[],[],[],[],[]]
    # *Creating a list with 5 rows with 5 words each
    #appending a row 5 times
    for i in range(5):
        #creating the row
        for _ in range(5):
            word = random.choice(names)
            board[i].append(word[::-1])
            names.remove(word)
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
        print('-------------------------------------------')


def main():
    # names = aligning_words(names_for_a_game)
    # print_players_board(names)
    # print(names_for_a_game)
    print_agents_board(NUM_OF_COLORS, starter)


if __name__ == '__main__':
    main()