grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# task 1
print('Sorting in 321 order.')
grades.sort(reverse=True)
print(grades)

# task 2
grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
total = sum(grades)
print('Total', total)

print('Counting Students!')
student_count = grades.count ('Students')
print('Students Count:', student_count)

average_grade = total / 10
print('Average Grade:')
print(average_grade)

#task 3
# Replace any grade below 80 with the value Failed.

print('Any grade below 80 is FAILED.')
grades[7] = 'FAILED'
grades[8] = 'FAILED'
grades[9] = 'FAILED'
print(grades)
