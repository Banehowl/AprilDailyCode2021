# ---------------------------------------------------------------
# #	Daily Code	04/08/2021
#   "Is the Word Singular or Plural (s)" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------

# Create a function that takes in a word and determines whether or not it is plural.
# A plural word is one that ends in "s" in this case.

# is_plural("changes") -> True
# is_plural("change") -> False
# is_plural("dudes") -> True
# is_plural("magic") -> False

def is_plural(word):
    pluralCheck = word.endswith('s')
    if pluralCheck == True:
        return True
    else:
        return False

print is_plural("changes")
print is_plural("change")
print is_plural("dudes")
print is_plural("magic")