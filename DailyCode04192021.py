# -----------------------------------------
# #	Daily Code	04/19/2021
#   "Smash Factor" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------

# Smash factor is a term in golf that relates to the amount of energy transferred from the club head to the golf ball.
# The formula for calculating smash factor is ball speed divided by club speed.

# Create a function that takes ball speed bs and club speed cs as arguments and returns the smash factor to the
# nearest hundredth.

# smash_factor(139.4, 93.8) -> 1.49
# smash_factor(181.2, 124.5) -> 1.46
# smash_factor(154.7, 104.3) -> 1.48

def smash_factor(bs, cs):
    solution = round(bs/cs,2)
    return solution

print smash_factor(139.4, 93.8)
print smash_factor(181.2, 124.5)
print smash_factor(154.7, 104.3)