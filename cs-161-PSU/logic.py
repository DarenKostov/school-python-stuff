'''
Daren Kostov
Thierry Ndayisaba

Licence: GPLv3
https://www.gnu.org/licenses/gpl-3.0.en.html

This is part of the Escape Room Game
'''


#WIP game map
gameMapString=[
  "#####",
  "# j #",
  "# @t#",
  "#   #",
  "#####"
]



gameMap=[]


traversableThings=[" "]
player=(2, 2)



#====> the 2 while loops <====
#make the map into a 2d array
x=0
while x<len(gameMapString):
  y=0
  gameMap.append([])
  while y<len(gameMapString[0]):
    gameMap[x].append(gameMapString[y][x])
    y+=1
  x+=1

def printBoard():
  global gameMap

  #====> the 2 while loops <====
  y=0
  while y<len(gameMap[0]):
    x=0
    while x<len(gameMap):
      print(gameMap[x][y], end="")
      x+=1
    print()
    y+=1


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



printBoard()
movePlayer(-1, 0)
printBoard()
movePlayer(0, -1)
printBoard()


