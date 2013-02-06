from location import *

##########################################
#
#
# Rooms have a name, a location, and exits.
#
#
#
#
#
##########################################

class Room:

    def __init__(self, name, location, desc):
        self._name = name
        self._loc = location
        self._desc = desc

    def __str__(self):
        roomDesc = str(self._loc) + "\n" + self._name + self._desc + "\n" + "Exits: " + formatList(self._loc.findExits())
        return roomDesc

def formatList(listOf):
    strItem = "" 
    for item in listOf:
        strItem += str(item) + "  " 
    return strItem
