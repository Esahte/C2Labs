def encode(s):
    if len(s) == 0:
        return 0
    t = chr(ord(s[len(s)-1]) + 5)
    print(t, end='')
    encode(s[:-1])


p = str(input('Enter a word: '))
encode(p)
print()


def decode(x):
    if len(x) == 0:
        return 0
    y = chr(ord(x[0]) - 5)
    print(y, end='')
    decode(x[1:])


k = str(input('Enter a word: '))
decode(k)
