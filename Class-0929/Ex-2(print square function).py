# Create a function to print a n by n square using # sign

# def printSquare(n)

def printSquare(n):
    print('#' * n) #print the first line
    for i in range(1, n - 1):
        print('#' + ' ' * (n - 2) + '#') # print mid line multiple times
    print('#' * n) #print the last line

# call function printSquare
printSquare(5)