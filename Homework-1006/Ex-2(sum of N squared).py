# Write a function called getSquareSum(n)
# For the given integer n calculate the following sum and return the sum
# 1^2+2^2+3^2+.... n^2

def getSquareSum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i*i
    return total


print(getSquareSum(3))
