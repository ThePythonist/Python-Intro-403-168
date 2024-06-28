def is_binary(number):
    for i in number:
        if i in ["0", "1"]:
            pass
        else:
            return False

    return True


print(list(filter(is_binary,["1011", "12", "4", "1000"])))
