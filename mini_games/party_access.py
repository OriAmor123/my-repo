def main():
    age = input('please enter your age: ')
    if age.isnumeric():
        age=int(age)
        if 0< age <=16:
            print('you can\'t enter the party, sorry.')
        elif age ==17:
            print('you can\'t enter this year, but you\'ll be able to enter next year.')
        elif age >=18:
            print('you can enter the party, enjoy!') 
        else:
            print('invalid age')
    else:
        print('invalid age')

if __name__ == '__main__':
    main()