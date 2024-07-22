def my_filter1(file):
    file = file.split("\n")
    print(file)


f = open("words.txt").read()
my_filter1(f)


def my_filter2(file):
    for i in file[:20]:
        print(i[0:-1])


f = open("words.txt").readlines()
my_filter2(f)
