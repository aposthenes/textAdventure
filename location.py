from copy import deepcopy

#######################
#
# OH IT'S A LOCATION THING
# YOU KNOW, WITH FRICKIN' GRIDS AND STUFFS.
#
#######################

#Maybe I should move this loop somewhere else....perhaps
#in the test.py section so that it only executes once.
grid = []
fp = open("world.txt")
row = fp.readline()[:-1]
while(len(row) !=0):
    col = list(row)
    grid.append(col)
    row = fp.readline()[:-1]
fp.close()

class Location:

    def __init__(self, y, x):
        self._y = int(y)
        self._x = int(x)


    def __str__(self):
        """
        Returns a string in the form of (y, x)
        """
        strLoc = "(" + str(self._y) + ", " + str(self._x) + ")"
        return strLoc

    def __eq__(self, other):
        if((self._x == other._x) and (self._y == other._y)):
            return True
        else:
            return False

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def findExits(self):
        """
        This moves through the 2d array grid and finds
        whatever is not a character that should be ignored...
        """
        exits = []
        for i in range(self._y - 1, self._y + 2):
            for j in range(self._x - 1, self._x + 2):
                    if(grid[i][j] != "#" and (self != Location(i, j))):
                        exits.append(Location(i, j))
        return exits
             
    def gridLoc(self):
        global grid
        currentGridLoc = deepcopy(grid) 
        currentGridLoc[self._y][self._x] = "x"
        currGridStr = ""
        for i in range(len(currentGridLoc)):
            for j in range(len(currentGridLoc[0])):
                currGridStr += currentGridLoc[i][j] 
            currGridStr += "\n"
        return currGridStr

    def printGrid(self):
        global grid
        gridString =""
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                gridString += grid[i][j]
            gridString += "\n"
        print(gridString) 
    """
    TODO:
    for later usage: if the map ends up becoming too huge to have it printed to the player
    i need to find a way to only print parts of the map at a time. Perhaps limiting it to 
    8 blocks shown around the player... that actually just seems like fiddling with the i/j
    numbers a bit on the printGridLoc function above to be honest. I guess theren's nothing
    else to do in this file?
    """

