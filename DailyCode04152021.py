# -----------------------------------------------
# #	Daily Code	04/15/2021
#   "Convert Yen to USD" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------

# Create a function that can turn Yen (Japanese dollar) to USD (American dollar).

# yen_to_usd(1) -> 0.01
# yen_to_usd(500) -> 4.65
# yen_to_usd(649) -> 6.04

def yen_to_usd(num):
    convertYen = num / 107.5
    roundYen = round(convertYen,2)
    return roundYen

print yen_to_usd(1)
print yen_to_usd(500)
print yen_to_usd(649)