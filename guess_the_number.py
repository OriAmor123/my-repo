import random

secret_num= random.randint(1,11)
trys_available=5
current_try=0

guess = int(input('guess the number between 1-10: '))
while guess !=secret_num:
    if guess < secret_num:
        print('Too Low')
    else:
        print('Too High')
    current_try +=1
    if current_try == trys_available:
        break
    guess=int(input('Wrong! try again: '))

if trys_available > current_try:
    print('you guessed the number')
else:
    print(f'i\'m sorry, you used all your trys, the secret number was {secret_num}')