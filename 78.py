def ingwords(lines):
    ing_lst = []
    for i in lines:
        # if i[-4:] == "ing\n":
        if i[-4:-1] == "ing":
            ing_lst.append(i)

    print(ing_lst)


f = open("words.txt").readlines()
ingwords(f)
