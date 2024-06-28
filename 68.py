# def (x):
#     if type(x) in [int, float]:
#         return True
#     else:
#         return False

is_number = lambda x : True if type(x) in [int,float] else False

print(list(filter(is_number, ["Tokyo", 4, "Madrid", 12, 2.5, "London"])))
