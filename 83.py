def myfunc2(file):
    for i in file:
        print(i[::-1])


f = open("words.txt").readlines()
myfunc2(f)
