import random
CAPITAL_LETTERS = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SMALL_LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
NOTES_AVAILABLE = CAPITAL_LETTERS + SMALL_LETTERS + NUMBERS

#must begin with capital, must contain at least 1 from each class
#dedning a function that creates a password
def randomize():
    password = ''
    for i in range(8):
        if i==0:
            note = random.sample(CAPITAL_LETTERS, 1)[0]
            password+=note
            continue
        note = random.sample(NOTES_AVAILABLE,1)[0]
        password+=note
    return password

password = randomize()

#checks if the password contains small letters and numbers
while True:
    #checks if the password contains small letters
    for letter in SMALL_LETTERS:
        letter_check=0
        if letter in password:
            letter_check+=1
            break
    #checks if the password contains numbers
    for number in NUMBERS:
        number_check=0
        if number in password:
            number_check+=1
            break
    #checks if the password is according to the requirements,
    #else regenerates new password and checks it again
    if number_check>0 and letter_check >0:
        break
    else:
        password = randomize()

print(password)