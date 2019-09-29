# Apple Sharing

# Create two variables: numStudents and numApples
# Students take apples from a basket and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?

# Test with 20 apples, 6 students

numStudents = 6
numApples = 20

applesPerStudent = numApples // numStudents
applesLeft = numApples % numStudents

print('Each student gets', applesPerStudent, 'apples')
print('There are', applesLeft, 'apples left in the basket')

# Test with 25 apples, 10 students


