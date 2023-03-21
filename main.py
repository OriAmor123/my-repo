import mini_games.sqrt_of_complex_number as sqrt_of_complex_number
import games.Rock_Paper_Scissors as Rock_Paper_Scissors
import mini_games.quadratic_formula as quadratic_formula
import games.password_generator as password_generator
import games.Hangman as Hangman
import mini_games.party_access as party_access
import games.TicTacToe as TicTacToe
import games.betting_slot_machine as betting_slot_machine

def main():
    print('1 - "sqrt of complex number"\n2 - "rock paper scissors"\n3 - "quadratic formula"\n4 - "password generator"    \
          \n5 - "hangman"\n6 - "party access"\n7 - "TicTacToe"\n8 - "betting slot machine"')
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
        elif choose == '7':
            TicTacToe.main()
            break
        elif choose == '8':
            betting_slot_machine.main()
            break
        else:
            print('your input is invalid')

    


if __name__ == '__main__':
    main()