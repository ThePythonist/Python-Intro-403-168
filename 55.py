def check_prime(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    print("is prime") if len(divisors) == 2 else print("is composite")


check_prime(int(input("Enter any number : ")))
