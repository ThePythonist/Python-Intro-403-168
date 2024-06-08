# pythons = ["kiarash", "matin", "roya", "mahsa", "farshad"]
# icdls = ["javad", "matin", "mahsa", "mohammad"]
# common = []
#
# for i in pythons:
#     if i in icdls:
#         common.append(i)
#
# print(common)

# ----------------------------------------------

pythons = ["kiarash", "matin", "roya", "mahsa", "farshad"]
icdls = ["javad", "matin", "mahsa", "mohammad"]
common = []

for i in pythons:
    for j in icdls:
        if i == j:
            common.append(i)

print(common)
