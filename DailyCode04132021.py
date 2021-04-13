# ---------------------------------------------------
# #	Daily Code	04/13/2021
#   "Rotate the List by One" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------

# Given a list, rotates the values clockwise by one (the last value is sent to the first position).

# rotate_by_one([1, 2, 3, 4, 5]) -> [5, 1, 2, 3, 4]
# rotate_by_one([6, 5, 8, 9, 7]) -> [7, 6, 5, 8, 9]
# rotate_by_one([20, 15, 26, 8, 4]) -> [4, 20, 15, 26, 8]

def rotate_by_one(lst):
    newLst = lst[1:] + lst[:1]
    print lst[1:]
    print lst[:1]
    return newLst


print rotate_by_one([1, 2, 3, 4, 5])