# Factorial
# 4! = 4 x 3 x 2 x 1

# def factorial(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1 # Because factorial of 1 is 1 itelf.
#
#     return n * factorial(n-1) # which means 4 * (4-1)
#
# print(factorial(5))



def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"Factorial of {n} is: {factorial(n)}")