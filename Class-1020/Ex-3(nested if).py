"""
Learn the following code, understand how the nested conditional statements work
"""

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        # x is greater than 0, y is greater than 0
        print("Quadrant I")
    else:
        # x is greater than 0, y is less or equal than 0
        print("Quadrant IV")
else:
    if y > 0:
        # x is less or equal than 0, y is greater than 0
        print("Quadrant II")
    else:
        # x is less or equal than 0, y is less or equal than 0
        print("Quadrant III")