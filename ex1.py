#recieved numbers till recieved the letter 'q' and calculates the average
num = input('insect a number: ')
counter = 0 #the count on numbers inserted
average = 0
while num !='q':
    if not num.isnumeric():
        num = input('insect a number: ')
        continue
    else:
        average = (average*counter + float(num))/(counter+1) #doesn't work properly
        counter +=1
    num = input('insect a number: ')

print(average)