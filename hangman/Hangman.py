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

HANGMAN_PHOTOS = {
    'case 1': '    x-------x',
    'case 2': '    x-------x\n    |\n    |\n    |\n    |\n    |',
    'case 3': '    x-------x\n    |       |\n    |       0\n    |\n    |\n    |',
    'case 4': '    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |',
    'case 5': '    x-------x\n    |       |\n    |       0\n    |      /|\\ \n    |\n    |',
    'case 6': '    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |',
    'case 7': '    x-------x\n    |       |\n    |       0\n    |      /|\\ \n    |      / \\ \n    |'
}

#printing openning screen
def openning_screen():
    print(f'{OPENNING_SENTENCE} \n {HANGMAN_ASCII_ART}')
    print(f'number of tries available: {NUMBER_OF_TRYS}')

#checks if the guess is valid
def is_valid_input(guess):
    if len(guess) > 1 or not guess.isalpha():
        return False
    else:
        return True

#adding the current guess the the already guessed letters list
def update_letter_guessed(letter_guessed, old_guesses):
    if letter_guessed not in old_guesses:
        old_guesses.append(letter_guessed)
        return True
    else:
        return False

#showing letters
def show_hidden_word(secret_word, old_guesses):
    for letter in secret_word:
        if letter in old_guesses:
            print(f'{letter} ', end='')
        else:
            print('_ ', end='')
    print()

#checks if a player win
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

#printing the current case of the hangman after wrong guess
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[f'case {num_of_tries}'])

#choosing a word
import random
def choose_word(words):
    return random.sample(words, 1)

#the game
def main():
    current_try = 1
    already_guessed_letters = []
    #part 1 - openning and choosing a word
    openning_screen()
    word = choose_word(WORD_LIST)[0]
    show_hidden_word(word, already_guessed_letters)
    print_hangman(current_try)
    
    #part 2 - rounds
    while current_try < 7:
        guess = input('guess a letter: ')
        while not is_valid_input(guess) or not update_letter_guessed(guess, already_guessed_letters):
            print('X')
            for letter in already_guessed_letters:
                print(f'{letter}', end=' -> ')
            guess = input('guess a letter: ')
            if is_valid_input(guess) and update_letter_guessed(guess, already_guessed_letters):
                break
        if guess in word:
            show_hidden_word(word, already_guessed_letters)
        else:
            current_try+=1
            show_hidden_word(word, already_guessed_letters)
            print_hangman(current_try)
        if check_if_win(word, already_guessed_letters):
            break
    
    #part 3 - end of the game and results
    if current_try<7:
        print(f'You won!! \nThe word was {word}')
    else:
        print(f'Sorry, you used all your trys, the word was {word}')

if __name__ == '__main__':
    main()