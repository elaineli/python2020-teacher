# Print a 5 by 5 square using # sign

n = 5

print('#' * n)
for i in range(1, n-1):
    print('#' + ' ' * (n-2) + '#')
print('#' * n)
