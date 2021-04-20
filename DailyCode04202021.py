# --------------------------------------------
# #	Daily Code	04/20/2021
#   "Stack the Boxes" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------

# Some of the cubes are hidden behind other cubes. Model one consists of one cube. Model two consists of four
# cubes, and so on...

# Write a function that takes a number n and returns the number of stacked boxes in a model n levels high,
# visible and invisible.

# stack_boxes(1)-> 1
# stack_boxes(2) -> 4
# stack_boxes(0) -> 0

def stack_boxes(n):
    if n <= 0:
        return "0"
    else:
        solution = n**n
        return solution

print stack_boxes(1)
print stack_boxes(2)
print stack_boxes(0)