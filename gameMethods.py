from room import Room
import location

def genRooms(fileName):
    """
    This method is really only a one-time use. You just need
    to input the fileName and it should return an array of Rooms.
    TODO: There must be a neater way of looping through the file pointer.
    """
    fp = open(fileName, "r")
    moreLines = True
    roomList = []
    for i in range(len(location.grid)):
        roomList.append([None] * len(location.grid[0]))
    while(moreLines):
        roomLocLine = fp.readline()[6:].split()
        roomY = int(roomLocLine[0])
        roomX = int(roomLocLine[1])
        roomLocation = location.Location(roomY, roomX)
        roomName = fp.readline()[7:]
        roomDesc = fp.readline()[7:]
        roomList[roomY][roomX] = Room(roomName, roomLocation, roomDesc)
        nextLine = fp.readline().rstrip("\n")

        if(nextLine == "end"):
            moreLines = False

    fp.close()
    return roomList



