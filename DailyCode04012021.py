# -----------------------------------------
# #	Daily Code	04/01/2021
#   "Sum of Cubes" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------

# Create a function that takes a positive integer n, and returns the sum of all the cubed values from 1 to n.

# For example, if n is 3:
# sum_cubes(3) -> 36
# 1 ** 3 + 2 ** 3 + 3 ** 3 = 36

def sum_cubes(n):
    solution = (1 ** n) + (2 ** n) + (3 ** n)
    return solution

print sum_cubes(3)
