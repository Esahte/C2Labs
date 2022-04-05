from random import shuffle
# 1a:
var = [True for x in range(0, 40)]

# 1b:
var[39] = 54.5

# 1c:
var = [x for x in range(0, 40)]
sum(var[:3])
print(sum(var[:3]))

# 1d:
print(max(var))

# 1e:
shuffle(var)
print(var)

