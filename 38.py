shopping_list = [
    "khodkar", "kaghaz",
    "mouse", "keyboard",
    "khodkar", "mouse",
]

unique = []

for i in shopping_list:
    if i not in unique:
        unique.append(i)

print(unique)
