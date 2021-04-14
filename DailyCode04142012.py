# ---------------------------------------------
# #	Daily Code	04/14/2021
#   "Flip the Boolean" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# Due to a programming concept known as truthiness, certain values can be evaluated to (i.e. take the place of)
# booleans. For example, 1 (or any number other than 0) is often equivalent to True, and 0 is often
# equivalent to False.

# Create a function that returns the opposite of the given boolean, as a number.

# flip_bool(True) -> 0
# flip_bool(False) -> 1
# flip_bool(1) -> 0
# flip_bool(0) -> 1

def flip_bool(num):
    if num == 1:
        return "0"
    elif num == 0:
        return "1"
    elif num == True:
        return False
    elif num == False:
        return True

print flip_bool(True)
print flip_bool(False)
print flip_bool(1)
print flip_bool(0)