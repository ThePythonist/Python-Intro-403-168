f = open("names.txt", "w")
names = ["mohammad", "matin", "hossein", "niayesh", "setayesh", "najmeh"]
output = []
for i in names:
    output.append(i + "\n")

f.writelines(output)
