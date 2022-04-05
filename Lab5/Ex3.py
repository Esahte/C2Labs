# def inList(num, lst):
#     for i in lst:
#         if i > num:
#             break
#         elif i == num:
#             return f'{num} is in list'
#     return f'{num} is not in the list'

# def inList(num, lst):
#     i = 0
#     while num >= lst[i]:
#         if num == lst[i]:
#             return f'{num} is in the list'
#         i += 1
#     return f'{num} is not in the list'


def inList(num, lst):
    lst.sort()
    if search(num, lst):
        return f'{num} is in list'
    else:
        return f'{num} is not in list'


def search(no, lst2):
    if lst2[0] > no:
        return False
    elif lst2[0] == no:
        return True
    return search(no, lst2[1:])


def main():
    print(inList(6, [2, 5, 7, 9]))


main()
