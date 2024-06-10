# word = "python"
# chars = {}
#
# counter = 0
# for i in word:
#     chars.setdefault(counter, i)
#     counter += 1
#
# print(chars)

# =========================================================

# word = "engineer"
# chars = {}
#
# for i in range(len(word)):
#     chars.setdefault(i, word[i])
#
# print(chars)

# =========================================================

word = "python"
chars = dict(zip(range(len(word)),word))
print(chars)
