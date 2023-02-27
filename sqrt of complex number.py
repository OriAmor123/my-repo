print('the complex number is represented by "x+yi"')
x=float(input('enter x: '))
y=float(input('enter y: '))
import math
a1=y/(2*math.sqrt((-x+math.sqrt(x**2+y**2))/2))
b1=math.sqrt((-x+math.sqrt(x**2+y**2))/2)
a2=-a1
b2=-b1
if x==0:
    if b1<b2: # Checks if b1/b2 is neg, to ensure there's no -+
        print(f'the square root of the complex number {y}i is {a1}{b1}i or {a2}+{b2}i')
    else:
        print(f'the square root of the complex number {y}i is {a1}+{b1}i or {a2}{b2}i')
elif y==0:
    print(f'the square root of the complex number {x} is {b1}i or {b2}i')
else:
    if b1<b2: # Checks if b1/b2 is neg, to ensure there's no -+
        if y<0:
            print(f'the square root of the complex number {x}{y}i is {a1}{b1}i or {a2}+{b2}i')
        else:
            print(f'the square root of the complex number {x}+{y}i is {a1}{b1}i or {a2}+{b2}i')
    else:
        if y<0:
            print(f'the square root of the complex number {x}{y}i is {a1}+{b1}i or {a2}{b2}i')
        else:
            print(f'the square root of the complex number {x}+{y}i is {a1}+{b1}i or {a2}{b2}i')