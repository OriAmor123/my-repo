#recieved numbers till recieved the letter 'q' and calculates the average
num = input('insect a number: ')
counter = 0 #the count on numbers inserted
average = 0
while num !='q':
    if not num.isnumeric(): #checks if the input is not a number and continue
        num = input('insect a number: ')
        continue
    else:
        average = (average*counter + float(num))/(counter+1) #checks if the input is a number and adding the number to the average
        counter +=1
    num = input('insect a number: ')

print(average)