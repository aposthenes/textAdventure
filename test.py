from player import Player
from room import Room
import location

def main():
    
    print("Hello and welcome to the testing center.")
    game = True
    roomsList = genRooms()
    name = input("What is your name? ")
    print("Putting you in location (2, 3)")
    player = Player(name, location.Location(2, 3))
    print("You are now", player, "at location ", player.getLoc())

    while(game):
        roomX = player.getLoc().getX()
        roomY = player.getLoc().getY()
        print(format(str(player.getLoc().gridLoc()), str(roomsList[roomY][roomX])))
        prompt = input("$ ")
        if prompt == "quit":
            game = False
            break
        else:
            player.move(prompt)

def genRooms():
    fp = open("myRooms.txt", "r")
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


def format(str1, str2):
    str1 = str1.split("\n")
    str2 = str2.split("\n")
    formatted = ""

    if(len(str1) > len(str2)):
        for i in range(len(str2)):
            formatted += str1[i] + "    " + str2[i] + "\n"
        for j in range(len(str2), len(str1)):
            formatted += str1[j] + "\n"
    elif(len(str1) < len(str2)):
        for i in range(len(str1)):
            formatted += str1[i] + "    " + str2[i] + "\n"
        for j in range(len(str1), len(str2)):
            formatted += str2[j] + "\n"
    else:
        for i in range(len(str1)):
            formatted += str1[i] + "    " + str2[i] + "\n"

    formatted + formatted[:-1]
    return formatted
main()
