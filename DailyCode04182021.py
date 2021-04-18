# ---------------------------------------------
# #	Daily Code	04/18/2021
#   "Make My Way Home" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# You will be given a list, showing how far James travels away from his home for each day. He may choose to travel
# towards or away from his house, so negative values are to be expected.

# Create a function which calculates how far James must walk to get back home.

# distance_home([2, 4, 2, 5]) -> 13
# distance_home([-1, -4, -3, -2]) -> 10
# distance_home([3, 4, -5, -2]) -> 0

def distance_home(num):
    travelDistance = sum(num)
    if travelDistance < 0:
        travelDistance = travelDistance * -1
    return travelDistance

print distance_home([2, 4, 2, 5])
print distance_home([-1, -4, -3, -2])
print distance_home([3, 4, -5, -2])