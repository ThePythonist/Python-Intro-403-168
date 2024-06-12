def func1(number):
    digits = []
    number = str(number)
    for i in number:
        digits.append(int(i))

    return sum(digits)


def func2(number):
    SUM = 0
    number = str(number)
    for i in number:
        SUM += int(i)

    return SUM


print(func2(int(input("Enter any number : "))))
