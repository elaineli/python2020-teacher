# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n! = 1 * 2 * 3 ... * n
# Write a function getFactorial(n) to calculate the value n! and return it
# Don't use math module in this exercise.

def getFactorial(n):
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total


print(getFactorial(4))
