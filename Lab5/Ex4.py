def main():
    FN = input('Enter ur full name: ').split()
    Ins = ''.split()

    for i in FN:
        Ins += f'{i[0].upper()}.'

    Ins.pop()
    Ins = ''.join(Ins)
    print(Ins)


if __name__ == '__main__':
    main()
