def create(number, extention):
    for i in range(number):
        open(f'file{i + 1}.{extention}', 'w')


number = int(input("How many files ? "))
extention = input("Type of file ? ")

create(number, extention)
