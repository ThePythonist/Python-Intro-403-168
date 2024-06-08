c1 = [45, 1, 2, 5, 3, 4]
c2 = [44, 43, 42, 41]
c = c1 + c2
c.sort()
c = list(set(c))
print(c)
