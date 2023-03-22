def main():
    import math
    A=float(input('Please enter A: '))
    B=float(input('Please enter B: '))
    C=float(input('Please enter C: '))
    D = -B/(2*A)
    E=A*D**2 +B*D + C
    print(f'f(x)={A}x\u00b2+{B}x+{C}=0')
    #!!!!should add a detector if the point is min or max
    print(f'vertex:({round(D,2)},{round(E,2)})')
    if B**2 - 4*A*C >0:
        print(f'x1={round((-B + math.sqrt(B**2 - 4*A*C))/(2*A),2)}')
        print(f'x2={round((-B - math.sqrt(B**2 - 4*A*C))/(2*A),2)}')
    elif B**2-4*A*C==0:
        print(f'x={round(-B/(2*A),2)}')
    else:
        print('There is no intersections with X axis')

if __name__ == '__main__':
    main()