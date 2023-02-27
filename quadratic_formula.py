import math
A=float(input('Please enter A: '))
B=float(input('Please enter B: '))
C=float(input('Please enter C: '))
D = -B/(2*A)
E=A*D**2 +B*D + C
print(f'f(x)={A}x\u00b2+{B}x+{C}=0')
print(f'vertex:({D},{E})')
if B**2 - 4*A*C >0:
    print(f'x1={(-B + math.sqrt(B**2 - 4*A*C))/(2*A)}')
    print(f'x2={(-B - math.sqrt(B**2 - 4*A*C))/(2*A)}')
elif B**2-4*A*C==0:
    print(f'x={-B/(2*A)}')
else:
    print('There is no intersections with X axis')