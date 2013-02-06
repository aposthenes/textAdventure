import location
import room

def main():
    
    print("hello world.")
    strRoom = str(room.Room("Kitchen", location.Location(0, 5), "This is the description of a mother fucking living room. Why don't you just deal with it, you dumbass.\nThere are very few reasons to do this, you know.\nBut I know that you are a motherfucking dumbass, you dumbass.\nHere are a couple of other lines that you can mother fucking say. Yeah.\nYou're such a fucking dumbass. You are so awesome.\nYou are so awesome I love you. :) Heart kiss kiss.\nBye bye.:D"))

    current = location.Location(0, 5)
    strCurr = current.gridLoc()
    
    print(format(strCurr, strRoom))

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
    
    formatted = formatted[:-1]
    return formatted

main()
