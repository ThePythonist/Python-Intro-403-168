def longest1(x):
    x = x.split()
    lenghts = []
    for i in x:
        lenghts.append(len(i))

    maxlen = max(lenghts)

    for i in x:
        if len(i) == maxlen:
            print("Longest is :", i)


# longest1("Hafte baad felafel darim")

def longest2(x):
    x = x.split()
    x.sort(key=len)
    print(x[-1])


# longest2("hafte baad felafel darim")

def longest3(x):
    x = x.split()
    print(max(x, key=len))


longest3("hafte baad felafel darim")
