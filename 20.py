students = ["hamed", "helia", "ahmad", "yahya"]

name = input("Enter your name : ")

# if "ali" in name[0:3]:
if name[0:3] == "ali":
    students.append(name)

print(students)
