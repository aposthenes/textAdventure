import location
########################################
#
# this is the player class
#
########################################
class Player:

    def __init__(self, playerName, playerLoc):
        self._name = playerName 
        self._loc = playerLoc
        
    def __str__(self):
        char = self._name
        return char
    
    def moveNorth(self):
        self._loc.setY(self._loc.getY() - 1)

    def moveSouth(self):
        self._loc.setY(self._loc.getY() + 1)

    def moveWest(self):
        self._loc.setX(self._loc.getX() - 1)
    
    def moveEast(self):
        self._loc.setX(self._loc.getX() + 1)

    def move(self, direction):
        north = location.Location(self._loc._y - 1, self._loc._x)
        south = location.Location(self._loc._y + 1, self._loc._x)
        west = location.Location(self._loc._y, self._loc._x - 1)
        east = location.Location(self._loc._y, self._loc._x + 1)
        
        if((direction == "n" or direction == "north") and self.canMove(north)):
            self.moveNorth()
            self._loc.printGridLoc()
        elif((direction == "s" or direction == "south") and self.canMove(south)):
            self.moveSouth() 
            self._loc.printGridLoc()
        elif((direction == "w" or direction == "west") and self.canMove(west)):
            self.moveWest() 
            self._loc.printGridLoc()
        elif((direction == "e" or direction == "east") and self.canMove(east)):
            self.moveEast() 
            self._loc.printGridLoc()
        else:
            print("You can't move that way.")
    
    def canMove(self, nextMove):
        exits = self._loc.findExits()
        for place in exits:
            if(nextMove == place):
                return True
        return False

"""
The move function definitely needs some more refining, but I'll leave it be for the moment..."
"""
