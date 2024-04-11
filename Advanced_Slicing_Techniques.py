# Objective: The aim of this assignment is to master the art of slicing in Python lists.
# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.
# Task 1: Given the list of temperatures:

# Extract the temperatures for the second week (7 days) of the week. Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week = ['83','85','86','87','88','89','90',]

week = temperatures[7:13]
print(week)

# Task 2: Extract all the temperatures above 100.

temps_above_hundred = ['101','102','103','104','105','106']

temps_above_hundred = temperatures[24:29]
print(temps_above_hundred)
temps_below_hundred = temperatures[0:23] 
print(temps_below_hundred)


# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

print('Reversed List of Temperatures for Month')
temperatures.reverse()
print(temperatures)

temperatures = [106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 75, 72]

fifth_day = temperatures[4]
print(fifth_day)
tenth_day = temperatures[9] 
print(tenth_day)
