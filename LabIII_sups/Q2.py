list1 = [x for x in range(0, 10)]
matrix = [[list1[i], list1[i + 1]] for i in range(0, 10, 2)]
print(matrix)

# [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
