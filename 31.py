items = [12, 6.5, "BMW", 14, 5, 68.12, "Toyota"]
nums = []

for i in items:
    if type(i) == str:
        nums.append(i)

print(nums)
