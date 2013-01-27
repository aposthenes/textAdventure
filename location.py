from grid import *
#######################
#
# OH IT'S A LOCATION THING
# YOU KNOW, WITH FRICKIN' GRIDS AND STUFFS.
#
#######################


locCoord = []

"""
The following loop generates a list of values that correspond to the values
on the map, although it starts with 0.
"""
for i in range(len(grid)):
    for j in range(len(grid[0])):
        locCoord.append([i, j])

class Location:
    """
    Location needs coordinates (x, y)
    From Location(x, y), there are a number of possibilities.
    Does this Location possess any exits? Exit possibilities??

    """

    def __init__(self, x, y):
        """
        I mean,
        what could I put here really???
        """
        self._x = x
        self._y = y


    def __str__(self):
        """
        This is where the location in coordinates would be printed.
        """
        strLoc = "(" + str(self._x) + ", " + str(self._y) + ")"
        return strLoc 

    """
    Here are the canMove options
    How do I verify this? Needs to check the grid for movable objects. Should check whether the player is already standing in that spot...
    in other words, if Location = Location.
    """
