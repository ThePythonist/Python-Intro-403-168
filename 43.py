numbers = []

for i in range(3):
    entry = input('Entry :')
    try:
        entry = float(entry)
        # if str(entry)[-2:] == ".0":
        if entry == int(entry):
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        pass

print("Numbers : ",numbers)
