import random
player_wins = 0
computer_wins = 0
options = ['rock','paper','scissors']
player_choose = input('choose rock/paper/scissors or type q to quit from the game: ')
#rock=0, paper=1, scissors=2

while player_choose != 'q':
    computer_num = random.randint(0,2)
    computer_pick=options[computer_num]

    if player_choose not in options:
        player_choose = input('choose rock/paper/scissors or type q to quit from the game: ')
        continue

    print(f'the computer picked {computer_pick}')

    if computer_pick == 'rock' and player_choose=='paper':
        print('You won, 1 point added to you')
        player_wins+=1
    elif computer_pick=='rock' and player_choose=='scissors':
        print('Computer won, 1 point added to the computer')
        computer_wins+=1
    elif computer_pick == 'paper' and player_choose=='rock':
        print('Computer won, 1 point added to the computer')
        computer_wins+=1
    elif computer_pick == 'paper' and player_choose=='scissors':
        print('You won, 1 point added to you')
        player_wins+=1
    elif computer_pick == 'scissors' and player_choose=='rock':
        print('You won, 1 point added to you')
        player_wins+=1
    elif computer_pick == 'scissors' and player_choose=='paper':
        print('Computer won, 1 point added to the computer')
        computer_wins+=1
    else:
        print('Draw, no points added')
    player_choose = input('choose rock/paper/scissors or type q to quit from the game: ')


print('The Game Is Over!')
print(f'results: you\'ve won {player_wins} times and the computer\'ve won {computer_wins} times')
if player_wins < computer_wins:
    print('You lost')
elif player_wins> computer_wins:
    print('You Won')
else:
    print('Draw!')