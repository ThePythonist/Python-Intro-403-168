def longest1(x):
    x.sort(key=len)
    print(x[-1])
    print(len(x[-1]))


def longest2(x):
    print(max(x, key=len))
    print(len(max(x, key=len)))


def longest3(x):
    maxlen = len(max(x, key=len))
    for i in x:
        if len(i) == maxlen:
            print(i)


lines = open("words.txt").readlines()
# longest1(lines)
# longest2(lines)
longest3(lines)
