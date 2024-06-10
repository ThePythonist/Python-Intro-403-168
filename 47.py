scores = {
    "dini": 12,
    "riazi": 17,
    "arabi": 8,
    "fizik": 15,
    "zaban": 20,
}

for i,j in scores.items():
    if j>=10:
        print(i,": Passed")
    else:
        print(i,": Failed")

moadel = sum(scores.values()) / len(scores)
print(moadel)
