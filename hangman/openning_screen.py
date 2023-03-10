OPENNING_SENTENCE = 'Welcome to the game Hangman'

#printing "Hangman"
HANGMAN_ASCII_ART = (' _    _\
      \n | |  | | \
      \n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \
      \n |  __  |/ _` | \'_ \\ / _` | \'_ ` _ \\ / _` | \'_ \\ \
      \n | |  | | (_| | | | | (_| | | | | | | (_| | | | | \
      \n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \
      \n                      __/ |     \
      \n                     |___/')
#part 1 - openning
print(f'{OPENNING_SENTENCE} \n {HANGMAN_ASCII_ART}')

#part 2 - getting a word
word = input('Please enter a word: ')
BLANK_LETTERS = ' _' *len(word)
print(BLANK_LETTERS)
already_guessed_letters = []

#part 3 - guessing a letter
guessing_letter = input('Guess a letter: ').lower()

#checking the letter
def is_valid_input(guess, old_guesses):
    if len(guess) > 1:
        return False
    if not guess.isalpha():
        return False
    if len(guess)==1 and guess.isalpha():
        return True

# #trys available
# print('6')

# #case 1
# print('    x-------x')

# #case 2
# print('    x-------x\n\
#     |\n\
#     |\n\
#     |\n\
#     |\n\
#     |')

# #case 3
# print('    x-------x\n\
#     |       |\n\
#     |       0\n\
#     |\n\
#     |\n\
#     |')

# #case 4
# print('    x-------x\n\
#     |       |\n\
#     |       0\n\
#     |       |\n\
#     |\n\
#     |')

# #case 5
# print('    x-------x\n\
#     |       |\n\
#     |       0\n\
#     |      /|\\ \n\
#     |\n\
#     |')

# #case 6
# print('    x-------x\n\
#     |       |\n\
#     |       0\n\
#     |      /|\\\n\
#     |      /\n\
#     |')

# #case 7
# print('    x-------x\n\
#     |       |\n\
#     |       0\n\
#     |      /|\\ \n\
#     |      / \\ \n\
#     |')