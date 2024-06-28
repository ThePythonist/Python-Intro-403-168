x = 12
def func(x):
    return [i for i in range(1, x + 1) if x % i == 0]


output = map(func, [10, 12, 21])
print(list(output))
