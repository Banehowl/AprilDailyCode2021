# ------------------------------------------
# #	Daily Code	04/16/2021
#   "Invert a List" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------

# Create a function that takes a list of numbers lst and returns an inverted list.

# invert_list([1, 2, 3, 4, 5]) -> [-1, -2, -3, -4, -5]
# invert_list([1, -2, 3, -4, 5]) -> [-1, 2, -3, 4, -5]
# invert_list([]) -> []

def invert_list(lst):
    negativeList = [-i for i in lst]
    return negativeList

print invert_list([1, 2, 3, 4, 5])
print invert_list([1, -2, 3, -4, 5])