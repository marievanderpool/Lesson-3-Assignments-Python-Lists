# 3. Deep Dive into Python Lists
# Objective: The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement: You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

students = ["John", "Doe", "Jane","Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art","Dance"]

# Print the name, grade and activiy of students with a score below 80. Expected Outcome "Jane", 78, "Art"

Jane_the_failure = [students[2], grades[2], activities[2]]
print(Jane_the_failure)

# For the remaining students, grab their name directly from  the students list name in a new list named students_approved. 
# Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved= [students[0], students[1], students[3]]
print(students_approved)

