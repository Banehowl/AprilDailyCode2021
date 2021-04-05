# -------------------------------------------------------------------
# #	Daily Code	04/05/2021
#   "Triangle and Parallelogram Area Finder" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------------

# Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram")
# as input and calculates the area of that shape.

# area_shape(2, 3, "triangle") -> 3
# area_shape(8, 6, "parallelogram") -> 48
# area_shape(2.9, 1.3, "parallelogram") -> 3.77

def area_shape(base, height, shape):
    if shape == "triangle":
        areaTriangle = (base * height) / 2
        return areaTriangle
    elif shape == "parallelogram":
        areaParallelogram = base * height
        return areaParallelogram

print area_shape(2, 3, "triangle")
print area_shape(8, 6, "parallelogram")
print area_shape(2.9, 1.3, "parallelogram")