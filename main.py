import sqrt_of_complex_number
import Rock_Paper_Scissors
import quadratic_formula
import password_generator
import Hangman
import party_access

def main():
    print('1 - "sqrt of complex number"\n2 - "rock paper scissors"\n3 - "quadratic formula"\n4 - "password generator"\n5 - "hangman"\n6 - "party access"')
    while True:
        choose = input('Please enter a number for access into the folowing programs: ')
        if choose == '1':
            sqrt_of_complex_number.main()
            break
        elif choose == '2':
            Rock_Paper_Scissors.main()
            break
        elif choose == '3':
            quadratic_formula.main()
            break
        elif choose == '4':
            password_generator.main()
            break
        elif choose == '5':
            Hangman.main()
            break
        elif choose == '6':
            party_access.main()
            break
        else:
            print('your input is invalid')

    


if __name__ == '__main__':
    main()