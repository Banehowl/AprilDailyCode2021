# -------------------------------------------------------------------
# #	Daily Code	04/02/2021
#   "Compare Strings by Count of Characters" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------------

# Create a function that takes two strings as arguments and return either True or False depending on whether the
# total number of characters in the first string is equal to the total number of characters in the second string.

# comp("AB", "CD") -> True
# comp("ABC", "DE") -> False
# comp("hello", "edabit") -> False

def comp(txt1, txt2):
    lenTxt1 = len(txt1)
    lenTxt2 = len(txt2)
    if lenTxt1 == lenTxt2:
        return True
    else:
        return False