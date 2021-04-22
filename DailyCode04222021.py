# ------------------------------------------------------------------
# #	Daily Code	04/22/2021
#   "Find the Smallest and Biggest Numbers" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------------------------

# Create a function that accepts a list of numbers and return both the minimum and maximum numbers,
# in that order (as a list).

# min_max([1, 2, 3, 4, 5]) -> [1, 5]
# min_max([2334454, 5]) -> [5, 2334454]
# min_max([1]) -> [1, 1]

def min_max(lst):
    minNum = min(lst)
    maxNum = max(lst)
    newLst = [minNum, maxNum]
    return newLst

print min_max([1, 2, 3, 4, 5])
print min_max([2334454, 5])
print min_max([1])