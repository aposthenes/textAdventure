from player import *
from location import *

def main():
    
    print("Hello and welcome to the testing center.")
    game = True

    name = input("What is your name? ")
    print("Putting you in location (3, 2)")
    player = Player(name, Location(3,2))
    print("You are now ", player, "at location ", player._loc)

    while(game):
        prompt = input("$ ")
        if prompt == "quit":
            game = False
            break
        else:
            player.move(prompt)
            print("You are at ", player._loc, "with a low chance of survival.")

main()
