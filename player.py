import location
########################################
#
# this is the player class
#
########################################
class Player:

    def __init__(self, playerName, playerLoc):
        self._name = playerName 
        self._health = 100
        self._loc = playerLoc
        
    def __str__(self):
        char = self._name
        return char

    def healthBar(self):
        bar = "#" * int(self._health/10)
        return bar
    
    def attacked(self, damage):
        self._health -= damage
        print(self.healthBar()) 
        if(self._health == 0):
            print("You died! Game over.")

    def move(self, direction):
        north = location.Location(self._loc._y - 1, self._loc._x)
        south = location.Location(self._loc._y + 1, self._loc._x)
        west = location.Location(self._loc._y, self._loc._x - 1)
        east = location.Location(self._loc._y, self._loc._x + 1)
        
        if((direction == "n" or direction == "north") and self.canMove(north)):
            self._loc._y -= 1
            self._loc.printGridLoc()
        elif((direction == "s" or direction == "south") and self.canMove(south)):
            self._loc._y += 1
            self._loc.printGridLoc()
        elif((direction == "w" or direction == "west") and self.canMove(west)):
            self._loc._x -= 1
            self._loc.printGridLoc()
        elif((direction == "e" or direction == "east") and self.canMove(east)):
            self._loc._x += 1
            self._loc.printGridLoc()
        else:
            print("You can't move that way.")
    
    def canMove(self, nextMove):
        exits = self._loc.findExits()
        for place in exits:
            if(nextMove == place):
                return True
        return False
