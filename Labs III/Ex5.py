from Ex4 import unlucky


def mostUnlucky(x, y):
    yearlist = [y for y in range(x, y)]
    mostUnlucky = []
    for i in yearlist:
        if len(unlucky(i)) >= 2:
            mostUnlucky.append(i)
    return mostUnlucky


# def main():
#     print(mostUnlucky(2001, 2022))
#
#
# main()
