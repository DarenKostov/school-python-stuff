'''
Daren Kostov
Thierry Ndayisaba

Licence: GPLv3
https://www.gnu.org/licenses/gpl-3.0.en.html

This is part of the Escape Room Game
'''


#WIP game map
gameMapString=[
  "########################",
  "# t    #               #",
  "# @j     #########     #",
  "#                      #",
  "##~~~~~#~~~~~~~ #     ##",
  "# ~~~~~#~~~~~~~ #      #",
  "# ~~~~~#~~~~~~~ #      #",
  "# ~~~~~~~~~~~~~ #      #",
  "# ~~~~~~~~~#~~~ #      #",
  "#          #    #    ###",
  "# ######   #      #    #",
  "#                 #    #",
  "########################",
]

print(len(gameMapString[0]))
print(len(gameMapString))

gameMap=[]


traversableThings=[" ", "~"]
player=(2, 2)
visibility=49



#====> the 2 while loops <====
#make the map into a 2d array
x=0
while x<len(gameMapString[0]):
  y=0
  gameMap.append([])
  gameMap[x]=[]
  while y<len(gameMapString):
    # print(y)
    gameMap[x].append(0)
    gameMap[x][y]=gameMapString[y][x]
    y+=1
  x+=1

def printBoard():
  global gameMap

  for y in range(max(0, player[1]-visibility), min(player[1]+visibility, len(gameMap[0]))):
    for x in range(max(0, player[0]-visibility), min(player[0]+visibility, len(gameMap))):
      print(gameMap[x][y], end="")
    print()


def isTraversable(thing):
  global traversableThings
  
  for traversable in traversableThings:
    if thing==traversable:
      return True
  return False

def movePlayer(deltaX, deltaY):

  global gameMap
  global player
  
  if isTraversable(gameMap[player[0]+deltaX][player[1]+deltaY]):
    #swap player and the thing we move into
    temp=gameMap[player[0]+deltaX][player[1]+deltaY]
    gameMap[player[0]+deltaX][player[1]+deltaY]='@'
    gameMap[player[0]][player[1]]=temp

    #move the coordinates of the player
    player=(player[0]+deltaX, player[1]+deltaY)


# def updateGliders():
#   for x in range(1, len(gameMapString[0])-1):
#     for y in range(1, len(gameMapString)-1):
#       if 
  
  

# def updateMap():

  


printBoard()
# movePlayer(-1, 0)
# printBoard()
# movePlayer(0, -1)
# printBoard()


