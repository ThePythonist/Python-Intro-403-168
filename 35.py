tedad = int(input("How many numbers : "))
numbers = []

for i in range(tedad):
    x = int(input("Enter any number : "))
    numbers.append(x)

print("Maximum number is", max(numbers))
