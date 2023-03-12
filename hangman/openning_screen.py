OPENNING_SENTENCE = 'Welcome to the game Hangman'
HANGMAN_ASCII_ART = (' _    _\
      \n | |  | | \
      \n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \
      \n |  __  |/ _` | \'_ \\ / _` | \'_ ` _ \\ / _` | \'_ \\ \
      \n | |  | | (_| | | | | (_| | | | | | | (_| | | | | \
      \n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \
      \n                      __/ |     \
      \n                     |___/')
WORD_FILE = open('C:\\Users\\OriAmor\\Desktop\\Python\\hangman\\words.txt')
WORDS = WORD_FILE.read()
WORD_LIST = WORDS.split()
NUMBER_OF_TRYS = 6
already_guessed_letters = []

HANGMAN_PHOTOS = {
    'case 1': '    x-------x',
    'case 2': '    x-------x\n    |\n    |\n    |\n    |\n    |',
    'case 3': '    x-------x\n    |       |\n    |       0\n    |\n    |\n    |',
    'case 4': '    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |',
    'case 5': '    x-------x\n    |       |\n    |       0\n    |      /|\\ \n    |\n    |',
    'case 6': '    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |',
    'case 7': '    x-------x\n    |       |\n    |       0\n    |      /|\\ \n    |      / \\ \n    |'
}

#part 3 - guessing a letter
# guessing_letter = input('Guess a letter: ').lower()

def openning_screen():
    print(f'{OPENNING_SENTENCE} \n {HANGMAN_ASCII_ART}')
    print(f'number of tries available: {NUMBER_OF_TRYS}')

def is_valid_input(guess, old_guesses):
    if len(guess) > 1 or not guess.isalpha() or guess in old_guesses:
        return False
    else:
        return True

def update_letter_guessed(letter_guessed, old_guesses):
    if letter_guessed not in old_guesses and is_valid_input(letter_guessed, old_guesses):
        old_guesses.append(letter_guessed)
        return True
    else:
        print('You already guessed this letter')
        for letter in old_guesses:
            print(f'{letter}', end=' -> ')
        return False

#showing letters
def show_hidden_word(secret_word, old_guesses):
    for letter in secret_word:
        if letter in old_guesses:
            print(f'{letter} ', end='')
        else:
            print('_ ', end='')

def check_if_win(secret_word, old_guesses):
    length=len(secret_word)
    counter = 0
    for letter in secret_word:
        if letter in old_guesses:
            counter+=1
    if counter==length:
        return True
    else:
        return False

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[f'case {num_of_tries}'])


import random
def choose_word(words):
    return random.sample(words, 1)

def main():
    global word
    global BLANK_LETTERS
    #part 1 - openning
    openning_screen()
    word = choose_word(WORD_LIST)[0]
    BLANK_LETTERS = (' _')*len(word)
    print(BLANK_LETTERS)

if __name__ == '__main__':
    main()
