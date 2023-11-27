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
  "# t>   #               #",
  "# @j   v #########     #",
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


gameMap=[]

traversableThings=[" ", "~"]
breakableThings=["@", "="]
collectableThings=["$", "J", "*", "+"]
burnableThings=["=", "+"]


player=(2, 2)
visibility=4

inventory={
  "$": 0,
  "J": 0,
  "*": 0,
  "+": 3
}


#====> the 2 while loops <====
#make the map into a 2d char array
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

def swap(coord1, coord2):
  temp=gameMap[coord1[0]][coord1[1]]
  gameMap[coord1[0]][coord1[1]]=gameMap[coord2[0]][coord2[1]]
  gameMap[coord2[0]][coord2[1]]=temp

  

def movePlayer(deltaX, deltaY):

  global gameMap
  global player
  
  if isTraversable(gameMap[player[0]+deltaX][player[1]+deltaY]):
    #swap player and the thing we move into
    swap((player[0]+deltaX, player[1]+deltaY),
      (player[0], player[1]))

    #move the coordinates of the player
    player=(player[0]+deltaX, player[1]+deltaY)


def updateGlider(x, y, dx, dy, altState):
  if isTraversable(gameMap[x+dx][y+dy]):
    swap((x, y), (x+dx, y+dy))
  else:
    gameMap[x][y]=altState

  
def updateGliders():
  for x in range(1, len(gameMap)-1):
    for y in range(1, len(gameMap[0])-1):
      if gameMap[x][y]==">":
        updateGlider(x, y, 1, 0, "<")
      elif gameMap[x][y]=="<":
        updateGlider(x, y, -1, 0, ">")
      elif gameMap[x][y]=="^":
        updateGlider(x, y, 0, -1, "v")
      elif gameMap[x][y]=="v":
        updateGlider(x, y, 0, 1, "^")
        
  
  

def updateMap():
  updateGliders()
  


# printBoard()
# movePlayer(-1, 0)
# printBoard()
# movePlayer(0, -1)
# printBoard()


