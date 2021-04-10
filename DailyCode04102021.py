# ----------------------------------------------------------
# #	Daily Code	04/10/2021
#   "Word Without First Character?" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------------

# Create a function that takes a word and returns the new word without including the first character.

# new_word("apple") -> "pple"
# new_word("cherry") -> "herry"
# new_word("plum") -> "lum"

def new_word(word):
    sliceLetter = slice(1,6)
    sliceWord = word[sliceLetter]
    return sliceWord

print new_word("apple")
print new_word("cherry")
print new_word("plum")