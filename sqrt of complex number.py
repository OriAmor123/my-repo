print('the complex number is represented by "x+yi"')
x=float(input('enter x: '))
y=float(input('enter y: '))
import math
a1=y/(2*math.sqrt((-x+math.sqrt(x**2+y**2))/2))
b1=math.sqrt((-x+math.sqrt(x**2+y**2))/2)
a2=-y/(2*math.sqrt((-x+math.sqrt(x**2+y**2))/2))
b2=-math.sqrt((-x+math.sqrt(x**2+y**2))/2)
print(f'the square root of the complex number {x}+{y}i is {a1}+{b1}i or {a2}+{b2}i')