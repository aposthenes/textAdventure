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
        if(direction == "n" or direction == "north"):
            self._loc._y += 1
        elif(direction == "s" or direction == "south"):
            self._loc._y -= 1
        elif(direction == "w" or direction == "west"):
            self._loc._x -= 1
        elif(direction == "e" or direction == "east"):
            self._loc._x += 1
        else:
            print("?? Direction error.")


