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
        roomDesc = self._name + str(self._loc) + "\n" + self._desc
#       print(self._loc.findExits())
        return roomDesc
