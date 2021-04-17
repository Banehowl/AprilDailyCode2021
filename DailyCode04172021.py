# ------------------------------------------
# #	Daily Code	04/17/2021
#   "Broken Bridge" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------

# Create a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through).

# is_safe_bridge("####") -> True
# is_safe_bridge("## ####") -> False
# is_safe_bridge("#") -> True

def is_safe_bridge(str):
    if ' ' in str:
        return False
    else:
        return True

print is_safe_bridge("####")
print is_safe_bridge("## ####")
print is_safe_bridge("#")