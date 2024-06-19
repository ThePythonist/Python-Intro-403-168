def check_number(number):
    if number % 2 == 0:
        print("entry is even")
    else:
        print("entry is odd")


def is_number(entry):
    # if type(entry) in [int, float]:
    #     check_number(entry)
    # else :
    #     print("entry is not a number")

    try:
        entry = float(entry)
        if entry == int(entry):  # adad sahih
            check_number(entry)
        else:  # adad ashari
            print("entry is not integer")
    except ValueError:
        print("entry is not a number")


is_number(input("Entry : "))
