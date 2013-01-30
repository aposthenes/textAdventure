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
        north = location.Location(self._loc._x, self._loc._y + 1)
        south = location.Location(self._loc._x, self._loc._y - 1)
        west = location.Location(self._loc._x - 1, self._loc._y)
        east = location.Location(self._loc._x + 1, self._loc._y)
#        print(self.canMove(south))
#        print(south)
#        print("The above is if it could happen.")
        if((direction == "n" or direction == "north") and self.canMove(north)):
            self._loc._y += 1
        elif((direction == "s" or direction == "south") and self.canMove(south)):
            self._loc._y -= 1
        elif((direction == "w" or direction == "west") and self.canMove(west)):
            self._loc._x -= 1
        elif((direction == "e" or direction == "east") and self.canMove(east)):
            self._loc._x += 1
        else:
            print("?? Direction error.")
    
    def canMove(self, nextMove):
        exits = self._loc.findExits()  
        for place in exits:
            if(nextMove == place):
#                print("these are my exits")
#                print(place)
                return True
        return False
