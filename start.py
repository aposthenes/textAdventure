from player import *

###############################
#
# welcome to my text adventure.
#
#
##############################

def main():
    
    name = input("What is your name? ") 
    player = Player(name)
    print("Welcome, ", player, "let's start.")
    game = True
    print("Starting your game...")

    player = Player(name)
    
    while(game):
        command = input("# ")
        if (command == "quit"):
            game = False
            break
        elif(command == "s" or command == "south"):
            moveNorth() 
        elif(command == "fight" or command == "fight"):
            print("You attack a dragon!")
            player.attacked(5)
        else:
            if(len(command.split()) > 1):
                print("CAS: What? I can only understand one word at a time.\n Example: # north")
                print("CAS: to the author of this program: remember to implement words based on movement(for the repeating loop) and for things like items, etc etc!")
            else:
                print("CAS: I'm sorry, I don't understand that. Could you repeat your command?")

        if(player._health == 0):
            game = False

    print("Thank you for playing.")







main()
