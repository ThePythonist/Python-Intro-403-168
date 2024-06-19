balance = 0

print(balance)

def variz(x):
    print("dar hale variz ...")
    global balance
    balance += x


variz(500)
print(balance)
