num1 = int(input('insert a first number between 1-9: '))
num2 = int(input('insert a second number between 1-9: '))

#making sure that there is no duplicate guesses
while num2 == num1:
    print('you can\'t insert the same number twice')
    num2 = int(input('insert a second number between 1-9: '))

#choosing 2 numbers between 1-9
import random
rd_from_list = random.sample(range(1,10), 2)

#checks if the player guessed correctly
if num1 == rd_from_list[0] or num1==rd_from_list[1] or num2==rd_from_list[0] or num2==rd_from_list[1]:
    print('you\'ve guessed the number!!!')
else:
    print(f'sorry, there was not the number, the numbers were {rd_from_list}')
