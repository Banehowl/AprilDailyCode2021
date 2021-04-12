# ---------------------------------------
# #	Daily Code	04/12/2021
#   "Edaaaaabit" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------

# Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.

# how_many_times(5) -> "Edaaaaabit"
# how_many_times(0) -> "Edbit"
# how_many_times(12) -> "Edaaaaaaaaaaaabit"

def how_many_times(num):
    longA = "a" * num
    newEdabit = "Ed" + longA + "bit"
    return newEdabit

print how_many_times(5)
print how_many_times(0)
print how_many_times(12)