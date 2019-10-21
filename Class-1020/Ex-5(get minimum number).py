"""
Given two integers, print the smaller value.
"""
def getSmaller(m, n):
    if m < n:
        return m
    else:
        return n

print(getSmaller(11, 11))
print(getSmaller(11, 5))

"""
Given three integers, print the smallest value.
for example if l = 10, m = 20, n = 5, it should return 5
"""
def getSmallest(l, m, n):
    if l <= m and l <= n:
        return l
    if m <= l and m <= n:
        return m
    if n <= l and n <= m:
        return n

print(getSmallest(10, 20, 5))
print(getSmallest(10, 10, 5))
print(getSmallest(5, 10, 10))
print(getSmallest(20, 20, 40))

