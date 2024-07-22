def myfunc1(file):
    print(file[::-1])


f = open("words.txt").readlines()
myfunc1(f)
