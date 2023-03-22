import random
DICE_ART = {
    1: '┌─────────┐\n│         │\n│    ●    │\n│         │\n└─────────┘',
    2: '┌─────────┐\n│ ●       │\n│         │\n│       ● │\n└─────────┘',
    3: '┌─────────┐\n│ ●       │\n│    ●    │\n│       ● │\n└─────────┘',
    4: '┌─────────┐\n│ ●     ● │\n│         │\n│ ●     ● │\n└─────────┘',
    5: '┌─────────┐\n│ ●     ● │\n│    ●    │\n│ ●     ● │\n└─────────┘',
    6: '┌─────────┐\n│ ●     ● │\n│ ●     ● │\n│ ●     ● │\n└─────────┘'
}

def input_check():
    while True:
        dice = input('How many dices would you like to roll? ')
        if dice.isnumeric():
            return int(dice)
        else:
            print('Invalid number!')

def main():
    num_of_dices = input_check()
    sum_of_dices = 0
    for _ in range(num_of_dices):
        random_dice = random.randint(1,7)
        print(DICE_ART[random_dice])
        sum_of_dices+=random_dice
    print(f'The sum is {sum_of_dices}')



if __name__ == '__main__':
    main()