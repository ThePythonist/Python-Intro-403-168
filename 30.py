items = [12, 6.5, "BMW", 14, 5, 68.12, "Toyota"]
nums = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int,float]:
        nums.append(i)

print(nums)
