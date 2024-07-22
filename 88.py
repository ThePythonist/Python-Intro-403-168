import datetime


def show_age(birth):
    thisyer = datetime.datetime.now().year
    age = thisyer - birth
    print(age)


show_age(1991)
