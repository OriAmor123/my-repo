#מקבל רשימה של מספרים ומספר נוסף, מחזיר רשימה רק עם המספרים שמתחלקים במספר הנוסף
list1 = [1, 1, 1, 2,5,6,7,5,7,9,5,2,6,9,4]
module = int(input('enter a number: '))
new_list = []

for i in list1:
    if i%module==0:
        new_list.append(i)
print(new_list)