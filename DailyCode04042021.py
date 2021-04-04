# --------------------------------------------------
# #	Daily Code	04/04/2021
#   "Sum Greater Than Five" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------

# Write a function that returns the sum of elements greater than 5, in the given list.

# sum_five([1, 5, 20, 30, 4, 9, 18]) -> 77
# sum_five([1, 2, 3, 4]) -> 0
# sum_five([10, 12, 28, 47, 55, 100]) -> 252

def sum_five(lst):
    sumlst = []
    for i in lst:
        if i > 5:
            sumlst.append(i)
    solution = sum(sumlst)
    return solution

print sum_five([1, 5, 20, 30, 4, 9, 18])
print sum_five([1, 2, 3, 4])
print sum_five([10, 12, 28, 47, 55, 100])