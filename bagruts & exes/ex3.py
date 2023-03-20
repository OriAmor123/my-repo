#מקבל מילה, מחזיר נכון רק אם המילה שווה להיפוך שלה, אחרת מחזיר לא נכון
word=input('please enter a word: ')
reversed_word = word[::-1]
if word == reversed_word:
    print('True')
else:
    print('False')