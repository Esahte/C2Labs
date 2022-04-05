Lks = [False for o in range(100)]
S1 = 0
while S1 < len(Lks):
    Lks[S1] = True
    S1 += 1

Ts = 1
while Ts <= len(Lks):
    m = Ts
    while m < len(Lks):
        if not Lks[m]:
            Lks[m] = True
        else:
            Lks[m] = False

        m += Ts + 1
    Ts += 1

Ol = 0
while Ol < len(Lks):
    if Lks[Ol]:
        print(f'Locker {Ol} Open')

    Ol += 1
