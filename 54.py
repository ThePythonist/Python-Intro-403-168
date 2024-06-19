def is_binary(number):
    for i in number:
        if i in ["0", "1"]:
            pass
        else:
            return False

    return True


numbers = ["1011", "12", "4", "1000"]
for i in numbers:
    print(is_binary(i))
