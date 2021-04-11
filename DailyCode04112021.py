# ---------------------------------------
# #	Daily Code	04/11/2021
#   "Burrrrrrrp" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------

# Create a function that returns the string "Burp" with the amount of "r's" determined by the input
# parameters of the function.

# long_burp(3) -> "Burrrp"
# long_burp(5) -> "Burrrrrp"
# long_burp(9) -> "Burrrrrrrrrp"

def long_burp(num):
    longR = "r" * num
    newBurp = "Bu" + longR + "p"
    return newBurp

print long_burp(3)
print long_burp(5)
print long_burp(9)