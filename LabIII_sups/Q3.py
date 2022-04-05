a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
t = 0
for i in a:
    k = 0
    for j in i:
        print(f'a[{t}][{k}]={j}', end='   ')
        k += 1
    print()
    t += 1
