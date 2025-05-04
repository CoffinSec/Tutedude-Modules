
def factorial(x):
    if x < 2:
        return 1
    else:
        return x * factorial(x-1)

y = int(input("Enter a Number: "))
result=factorial(y)
print("Factorial of",y ,"is:", result)