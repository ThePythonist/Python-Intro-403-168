# nums = []
#
# for i in range(5):
#     x = int(input("Entry : "))
#     if 1 < x < 10:
#         nums.append(x)
#
# print(nums)

# =========================================================

nums = []

while len(nums) != 5:
    x = int(input("Entry : "))
    if 1 < x < 10:
        nums.append(x)

print(nums)
