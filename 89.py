from random import randint


def generate_password(length):
    password = ""

    for i in range(length):
        digit = str(randint(0, 9))
        password += digit

    print(password)


def generate_password2(length):
    password = []
    for i in range(length):
        digit = str(randint(0, 9))
        password.append(digit)

    output = "".join(password)
    print(output)


generate_password2(6)
