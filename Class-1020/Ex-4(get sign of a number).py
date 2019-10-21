"""
Write a function to check if a given number is greater, equal or less than 0
If the number is greater than 0, function should return 1
If the number is equal to 0, function should return 0
If the number is less than 0, function should return -1
"""

def getSign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

print(getSign(9))
print(getSign(-9))
print(getSign(0))