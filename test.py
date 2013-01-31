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
    print("You are now", player, "at location ", player._loc)

    while(game):
        row = player._loc.getY() 
        col = player._loc.getX()
        if(roomsList[row][col] != None):
            print(roomsList[row][col])
        else:
            print("Error: No room description entered for ", player._loc, "yet")
        prompt = input("$ ")
        if prompt == "quit":
            game = False
            break
        else:
            player.move(prompt)
            print("exits:")
            aList = player._loc.findExits()
            for exit in aList:
                print(exit)
            print("You are at ", player._loc, "with a low chance of survival.")

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

    for place in roomList:
        print(place)
    
    fp.close()
    
    return roomList
main()
