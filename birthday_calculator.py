birth_date=input('enter your birth date(using periods): ')
today=input('enter the date today(using periods): ')

birthday_split = birth_date.split('.')
today_split = today.split('.')

if birthday_split[0]==today_split[0] and birthday_split[1]==today_split[1]:
    print('you have a birthday today!!!')
else:
    print('you don\'t have a birthday today')
