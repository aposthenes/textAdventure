from player import Player
from room import Room
from methods import *
import location
import os 

def main():
    
    print("Hello and welcome to the testing center.")
    game = True
    roomsList = genRooms("myRooms.txt")
    name = input("What is your name? ")
    player = Player(name, location.Location(2, 3))
    os.system("clear")     

    while(game):
        roomX = player.getLoc().getX()
        roomY = player.getLoc().getY()
        currentLoc = str(player.getLoc().gridLoc())
        if(roomsList[roomY][roomX] is None):
            roomDesc = "NO ROOM DESCRIPTION"
            print(formatToStr(currentLoc, roomDesc))
        else: 
            convertRoom = str(roomsList[roomY][roomX])
            roomDesc = strBreak(convertRoom)
            print(formatToStr(currentLoc, roomDesc))

        prompt = input("$ ")
        if prompt == "quit":
            game = False
            os.system("clear") 
            break
        else:
            os.system("clear") 
            player.move(prompt)

main()
