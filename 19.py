students = ["amir", "behrad", "mehrnaz", "yasna"]

age = int(input("Enter your age : "))

if age >= 18:
    name = input("Enter your name : ")
    students.append(name)
    print(students)
else:
    print("You are not allowed")
