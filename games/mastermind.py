import random

NUMBERS_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUM_OF_ROUNDS = 10

def randomize_code(num_list):
    code = random.sample(num_list, 4)
    return code

#getting a guess from the player
def take_a_guess():
    while True:
        guess = input('Guess the code (Enter 4 numbers between 1-9, seperate using spaces): ')
        if len(guess.split())==4:
            for note in guess.split():
                if not note.isnumeric():
                    print('Invalid Guess!')
                    break
            else:
                for note in guess.split():
                    if not 1<=int(note)<=9:
                        print('Invalid Guess!')
                        break
                else:
                    break
            continue
        else:
            print('Invalid Guess!')
    return guess

def guess_check(guess_list, code):
    exist_in_place, exist_not_in_place = 0, 0

    for letter in guess_list:
        #checking each letter if it is contained within the code
        if letter in code:
            #the letter is in the code, checks if it is in the right place.
            if guess_list.index(letter) == code.index(letter):
                exist_in_place+=1
            else:
                exist_not_in_place+=1
    return exist_in_place, exist_not_in_place

#printing the board of the old guesses
def print_old_guesses(old_guesses):
    #each tuple: (in_place, guess, not_in_place)
    for round in old_guesses:
        print(f'Round {old_guesses.index(round)+1:2d}: In place: {round[0]} | {round[1]} | Not in place: {round[2]}')
    print('-------------------------------------------------')

def one_round(code, old_guesses):
    #taking the player's guess
    guess = take_a_guess()
    guess_list = guess.split()
    #checking if the player guessed correctly
    in_place, not_in_place = guess_check(guess_list, code)

    #creates a tuple from the current guess and the amount of in place and not in place
    old_guesses.append((in_place, guess, not_in_place))
    print_old_guesses(old_guesses)
    #returns True if the player guessed correctly
    if in_place == 4:
        print('Congratulations!! You\'ve guess the code')
        return True


def main():
    secret_code = randomize_code(NUMBERS_LIST)
    old_guesses = []
    print('Wellcome To Mastermind Game')
    print('Your mission is to guess a four digit code')
    print('The code is built from different numbers (Can\'t have 2 same numbers)')
    print(f'You have {NUM_OF_ROUNDS} trys\nGood Luck!!')
    for _ in range(NUM_OF_ROUNDS):
        if one_round(secret_code, old_guesses):
            break
    else:
        print(f'You\'ve used all your trys, the code was {secret_code}')



if __name__ == '__main__':
    main()