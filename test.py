from player import *
import location
from grid import *

def main():
    
    print("Hello and welcome to the testing center.")
    game = True

    name = input("What is your name? ")
    print("Putting you in location (2, 3)")
    player = Player(name, location.Location(2, 3))
    print("You are now ", player, "at location ", player._loc)

    while(game):
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
        print(grid)


main()
