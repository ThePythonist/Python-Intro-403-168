employees_income_402 = {
    "ali": 10000,
    "saman": 11500,
    "shahin": 9700,
}

print(employees_income_402)

employees_income_403 = {}

for i, j in employees_income_402.items():
    hoqoq = ((j * (25 / 100)) + j) - 1500
    employees_income_403.setdefault(i, hoqoq)
    # print(i,":",hoqoq)

print(employees_income_403)
