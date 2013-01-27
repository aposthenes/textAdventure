from player import *
import location

def main():
    
    print("Hello and welcome to the testing center.")
    game = True

    name = input("What is your name? ")
    print("Putting you in location (3, 2)")
    player = Player(name, location.Location(3,2))
    print("You are now ", player, "at location ", player._loc)

    while(game):
        prompt = input("$ ")
        if prompt == "quit":
            game = False
            break
        else:
            player.move(prompt)
            print("You are at ", player._loc, "with a low chance of survival.")

    print("Here are the possible exit locations.")
    player._loc.findExits()

main()
