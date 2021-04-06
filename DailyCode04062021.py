# ------------------------------------------------------
# #	Daily Code	04/06/2021
#   "Half, Quarter, and Eighth" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------------

# Create a function that takes a number and return a list of three numbers: half of the number, quarter
# of the number and an eighth of the number.

# half_quarter_eighth(6) -> [3, 1.5, 0.75]
# half_quarter_eighth(22) -> [11, 5.5, 2.75]
# half_quarter_eighth(25) -> [12.5, 6.25, 3.125]

def half_quarter_eighth(num):
    solutionList = []
    halfSolution = num * .5
    quarterSolution = num * .25
    eighthSolution = num * .125
    solutionList.append(halfSolution)
    solutionList.append(quarterSolution)
    solutionList.append(eighthSolution)
    return solutionList

print half_quarter_eighth(6)
print half_quarter_eighth(22)
print half_quarter_eighth(25)