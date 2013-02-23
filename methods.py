from room import Room
import location

def genRooms(fileName):
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


def formatToStr(str1, str2):
    map1 = str1.split("\n")
    desc2 = str2.split("\n")
    formatted = ""

    if(len(map1) > len(desc2)):
        for i in range(len(desc2)):
            formatted += map1[i] + "    " + desc2[i] + "\n"
        for j in range(len(desc2), len(map1)):
            formatted += map1[j] + "\n"
    elif(len(map1) < len(desc2)):
        for i in range(len(map1)):
            formatted += map1[i] + "    " + desc2[i] + "\n"
        for j in range(len(map1), len(desc2)):
            formatted += desc2[j] + "\n"
    else:
        for i in range(len(map1)):
            formatted += map1[i] + "    " + desc2[i] + "\n"

    formatted + formatted[:-1]
    return formatted

def strBreak(fullString):
    strList = fullString.split(" ")
    lenList = len(strList)
    choppedString = ""
    
    if(lenList > 20):
        count = 0 
        for i in range(int(lenList / 20)):
            for j in range(20):
                choppedString += strList[count] + " "
                count += 1
            choppedString += "\n"
        choppedString = choppedString[:-1]
        for k in range(lenList % 20 - 1):
            choppedString += strList[count] + " "
            count += 1
        return choppedString
    else:
        return fullString
