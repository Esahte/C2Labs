from Ex3 import Complex


def main():
    a, b = eval(input("Enter the first complex number: "))

    c1 = Complex(a, b)
    c, d = eval(input("Enter the second complex number: "))
    c2 = Complex(c, d)
    print(f'{c1} + {c2} = {c1 + c2}')
    print(f'{c1} - {c2} = {c1 - c2}')
    print(f'{c1} * {c2} = {c1 * c2}')
    print(f'{c1} / {c2} = {c1 / c2}')
    print(f'|{str(c1)}| = {str(abs(c1))}')


main()
