# Write a function called getSum(n)
# For the given integer n calculate the following sum: 1+2+...+n and return it
# If n = 5, the function should return 1 + 2 + 3 + 4 + 5 => 15

def getSum(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total

print(getSum(6))