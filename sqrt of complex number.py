print('the complex number is represented by "x+yi"')
x=float(input('enter x: '))
y=float(input('enter y: '))
import math
a1=y/(2*math.sqrt((-x+math.sqrt(x**2+y**2))/2))
b1=math.sqrt((-x+math.sqrt(x**2+y**2))/2)
a2=-y/(2*math.sqrt((-x+math.sqrt(x**2+y**2))/2))
b2=-math.sqrt((-x+math.sqrt(x**2+y**2))/2)
if x==0:
    print(f'the square root of the complex number {y}i is {a1}+{b1}i or {a2}+{b2}i')
elif y==0:
    print(f'the square root of the complex number {x} is {b1}i or {b2}i')
else:
    print(f'the square root of the complex number {x}+{y}i is {a1}+{b1}i or {a2}+{b2}i')
print(a1, a2)