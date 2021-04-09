# --------------------------------------------------------
# #	Daily Code	04/09/2021
#   "Is the Last Character an N?" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------

# Create a function that takes a string (a random name). If the last character of the name is an "n",
# return True, otherwise return False.

# is_last_character_n("Aiden") -> True
# is_last_character_n("Piet") -> False
# is_last_character_n("Bert") -> False
# is_last_character_n("Dean") -> True

def is_last_character_n(name):
    letterCheck = name.endswith('n')
    if letterCheck == True:
        return True
    else:
        return False

print is_last_character_n("Aiden")
print is_last_character_n("Piet")
print is_last_character_n("Bert")
print is_last_character_n("Dean")