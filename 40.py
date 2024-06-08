number = int(input("Enter any number : "))
divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

# if divisors == [1,number]:
if len(divisors) == 2:
    print(number, "is prime")
else:
    print(number, "is composite")
