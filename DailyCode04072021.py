# --------------------------------------------------------------------
# #	Daily Code	04/07/2021
#   "Check if a List Contains a Given Number" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------------

# Write a function to check if a list contains a particular number

# check([1, 2, 3, 4, 5], 3) -> True
# check([1, 1, 2, 1, 1], 3) -> False
# check([5, 5, 5, 6], 5) -> True
# check([], 5) -> False

def check(lst, num):
    if num in lst:
        return True
    else:
        return False

print check([1, 2, 3, 4, 5], 3)
print check([1, 1, 2, 1, 1], 3)
print check([5, 5, 5, 6], 5)
print check([], 5)