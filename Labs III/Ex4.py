from Ex3 import day_of_week


def unlucky(y):
    toughLuck = [(d, m, y) for m in range(1, 13) for d in range(1, 32) if d == 13 and day_of_week(d, m, y) == 'Friday']
    return toughLuck

# def unlucky(y):
#     toughLuck = []
#     for m in range(1, 13):
#     # for d in range(1, 32):
#         for d in range(1, 32):
#         # for m in range(1, 13):
#             if d == 13 and day_of_week(d, m, y) == 'Friday':
#                 toughLuck.append((d, m, y))
#     return toughLuck


# def main():
#     print(unlucky(2022))
#
#
# main()
