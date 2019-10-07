# First Write a function to repeat random string s n times, where s, n are the two parameters of this function
# Then Call this function with the string and the repetition you like

def repeatMe(str, numRepeats, name):
    returnedStr = ''
    for i in range(numRepeats):
        returnedStr += (str + ":" + name) + '\n'
    return returnedStr


print(repeatMe('hello there', 10, 'elaine'))