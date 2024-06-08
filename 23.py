numbers = (144, 128, 984, 256)

number = int(input("Enter any number : "))

if number % 2 == 0 and 99 < number < 1000:
    numbers += (number,)

print(numbers)
