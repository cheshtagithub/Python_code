n = int(input("Enter the number for factorial: "))
try:
    if (n == 0) or (n == 1):
        print(f"Factorial of {n} is: ",1)

    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(f"Factorial of {n} is:", fact)
except ValueError as e:
    print("invalid input:", e)
