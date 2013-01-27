##########################################
#
#
#
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
        print(self._name)
        print(self._loc)
