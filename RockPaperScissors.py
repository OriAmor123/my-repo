import random
player_wins = 0
computer_wins = 0
options = ['rock','paper','scissors']
#rock=0, paper=1, scissors=2

#checks who won the current game
def check_win(player, computer):
    global player_wins
    global computer_wins
    if computer == 'rock' and player=='paper':
        print('You won, 1 point added to you')
        player_wins+=1
    elif computer=='rock' and player=='scissors':
        print('Computer won, 1 point added to the computer')
        computer_wins+=1
    elif computer == 'paper' and player=='rock':
        print('Computer won, 1 point added to the computer')
        computer_wins+=1
    elif computer == 'paper' and player=='scissors':
        print('You won, 1 point added to you')
        player_wins+=1
    elif computer == 'scissors' and player=='rock':
        print('You won, 1 point added to you')
        player_wins+=1
    elif computer == 'scissors' and player=='paper':
        print('Computer won, 1 point added to the computer')
        computer_wins+=1
    else:
        print('Draw, no points added')

def main():
    player_choose = input('choose rock/paper/scissors or type q to quit from the game: ')
    while player_choose != 'q':
        if player_choose not in options:
            player_choose = input('choose rock/paper/scissors or type q to quit from the game: ')
            continue
        computer_num = random.randint(0,2)
        computer_pick=options[computer_num]
        print(f'the computer picked {computer_pick}')
        check_win(player_choose, computer_pick)
        player_choose = input('choose rock/paper/scissors or type q to quit from the game: ')
    
    #when the player chose "q"
    print('The Game Is Over!')
    print(f'results: you\'ve won {player_wins} times and the computer\'ve won {computer_wins} times')
    if player_wins < computer_wins:
        print('You lost')
    elif player_wins > computer_wins:
        print('You Won')
    else:
        print('Draw!')

if __name__ == '__main__':
    main()