numbers = []

while True:
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
    if entry == "exit":
        break

print(numbers)
