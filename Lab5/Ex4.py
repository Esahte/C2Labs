FN = input('Enter ur full name: ').split()
Ins = ''.split()

for i in FN:
    Ins += f'{i[0].upper()}.'

Ins.pop()
Ins = ''.join(Ins)
print(Ins)

