five_letters = []


def read_words():
    lines = open("words.txt").readlines()
    global five_letters

    for i in lines:
        if len(i) == 6:
            five_letters.append(i)


def write_words(five_letters):
    open("five_letters.txt", "w").writelines(five_letters)


read_words()
write_words(five_letters)
