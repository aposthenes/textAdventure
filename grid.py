##########################
#
# I did it wrong...
# Location should refer to grid
#
#########################
grid = []
fp = open("world.txt")
row = fp.readline()[:-1]
while(len(row) != 0):
    col = list(row)
    grid.append(col)
    row = fp.readline()[:-1]
fp.close()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j] != "#"):
            token = "*" 
        else:
            token = " "
        print(str(i) + "x" + str(j), end=token) 
    print()
            

class Grid: 
    def __init__(self):
        pass

    def __str__(self):
        gridString = ""
        global grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                gridString += grid[i][j] 
            gridString+= "\n"
        return gridString


    def isValid(self, block):
        """
        This is not actually in use yet. Dead function.
        """
        if(block == "o"):
            return False
        else: 
            return True
