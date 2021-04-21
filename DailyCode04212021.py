# ----------------------------------------------------------
# #	Daily Code	04/21/2021
#   "Recreating the abs() Function" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------------

# The abs() function returns the absolute value of a number. This means it returns a number's positive value.
# You can think of it as the distance away from zero.

# Create a function that recreates this functionality.

# absolute(-5) -> 5
# absolute(-3.14) -> 3.14
# absolute(250) -> 250

def absolute(num):
    if num < 0:
        newNumber = num * -1
        return newNumber
    else:
        return num

print absolute(-5)
print absolute(-3.14)
print absolute(250)