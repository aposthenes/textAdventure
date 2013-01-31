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

    def __init__(self, name, location):
        self._name = name
        self._loc = location

    def __str__(self):
        roomDesc = self._name + str(self._loc)
#       print(self._loc.findExits())
        return roomDesc
