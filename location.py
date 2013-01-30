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
on the map in the grid, although it starts with 0.
NOTE: I don't know if I actually NEED this for anything yet.
I probably don't, this loop may be overkill and redundant.
"""
for i in range(len(grid)):
    for j in range(len(grid[0])):
        locCoord.append([i, j])

class Location:

    def __init__(self, y, x):
        self._y = y 
        self._x = x 


    def __str__(self):
        """
        This is where the location in coordinates would be printed.
        """
        strLoc = "(" + str(self._y) + ", " + str(self._x) + ")"
        return strLoc

    def __eq__(self, other):
        if((self._x == other._x) and (self._y == other._y)):
            return True
        else:
            return False

    def findExits(self):
        """
        This moves through the 2d array grid and finds
        whatever is not a character that should be ignored...
        """
        exits = []
        for i in range(self._y - 1, self._y + 2):
            for j in range(self._x - 1, self._x + 2):
                    if(grid[i][j] != "#"):
                        exits.append(Location(i, j))
        return exits
               

    """
    TODO:

    what about canMove? Do objects have a location? They should move with the player. OMFG why is this so hard. what do i do...
    Forget this, I am moving onto Room objects.
    """

