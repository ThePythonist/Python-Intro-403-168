people = {
    "meysam": 30,
    "mohammadreza": 23,
    "mostafa": 33,
    "alaleh": 20,
    "shahram": 17
}

maxage = max(people.values())
oldest = ""

for i in people:
    if people[i] == maxage:
        oldest = i

print(oldest,":",maxage)
