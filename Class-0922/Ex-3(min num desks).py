# School desks
# A school decided to replace the desks in three classrooms.
# Each desk sits two students. Given the number of students in each class,
# print the smallest possible number of desks that can be purchased.

# Print number of desks needed if A class has 21 students, B class has 22 students, C class has 19 students

studentsA = 21
studentsB = 22
studentsC = 19

desks = studentsA // 2 + studentsA % 2 + studentsB // 2 + studentsB % 2 + studentsC // 2 + studentsC % 2

print('Total desk needed is', desks)