# Write a function named right_justify that takes a string named s as a parameter and
# prints the string with enough leading spaces so that the last letter of the string
# is in column 70 of the display.


def right_justify(s):
    num_of_spaces = 70-len(s)
    print(" "*num_of_spaces+s)


print("<"*70)
right_justify("hello there")