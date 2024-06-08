class_403_a = {
    "teacher": "sadeghi",
    "students": ["setayesh", "hossein", "mamad", "matin", "niayesh", "najmeh"],
    "time": [
        {"1shanbe": "17:00-18:30"},
        {"3shanbe": "17:00-18:30"},
    ],
    "level": "intermediate",
}

key = input("Search any key : ")

# if key in class_403_a:
#     print("found :", class_403_a[key])
# else:
#     print("key not found")

try:
    print(class_403_a[key])
except KeyError:
    print("key not found")
