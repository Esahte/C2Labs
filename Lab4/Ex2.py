t = input('Enter numbers: ')
repeats = 0
i = 1
while i < len(t):
    if t[i] == t[0]:
        repeats += 1
    i += 1
print(f'the number {t[0]} repeats {repeats} times')
