# ---------------------------------------------------------
# #	Daily Code	04/24/2021
#   "Check if All Values Are True" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------

# Create a function that returns True if all parameters are truthy, and False otherwise.

# all_truthy(True, True, True) -> True
# all_truthy(True, False, True) -> False
# all_truthy(5, 4, 3, 2, 1, 0) -> False

def all_truthy(*args):
    for i in args:
        status = all(args)
        if status == True:
            return True
        else:
            return False

print all_truthy(True, True, True)
print all_truthy(True, False, True)
print all_truthy(5, 4, 3, 2, 1, 0)