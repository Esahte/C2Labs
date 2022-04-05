from InsertionSort import insertionSort


lst = input('Enter a list of numbers: ').split()
lst2 = [int(i) for i in lst]
lst3 = [int(i) for i in lst]

if insertionSort(lst2) == lst3:
    print('is in ascending order')
else:
    print('is not in ascending order')
