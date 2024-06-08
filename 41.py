primes = []

for i in range(2, 100): # i == 5
    for j in range(2, i): # 2 ta 5
        if i % j == 0: # 5 % 2, 5 % 3, 5 % 4
            break
    else:
        primes.append(i)

print(primes)
