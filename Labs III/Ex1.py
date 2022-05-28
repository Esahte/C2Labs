Lks = [False for o in range(100)]

for Ts in range(len(Lks)):
    m = Ts
    while m < len(Lks):
        Lks[m] = not Lks[m]

        m += Ts + 1
# for i in range(1, len(Lks) + 1):
#     for j in range(i - 1, len(Lks), i):
#         Lks[j] = not Lks[j]


for Ol in range(len(Lks)):
    if Lks[Ol]:
        print(f'Locker {Ol + 1} Open')

