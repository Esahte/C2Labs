from Ex1 import LinearEquation


def main():
    a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: '))

    LE = LinearEquation(a, b, c, d, e, f)
    if LE.isSolvable():
        print(f'x is {LE.getX()} and y is {LE.getY()}')
    else:
        print('The equation has no solution')


main()
