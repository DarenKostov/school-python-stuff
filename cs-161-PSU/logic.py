'''
Daren Kostov
Thierry Ndayisaba

Licence: GPLv3
https://www.gnu.org/licenses/gpl-3.0.en.html

This is part of the Escape Room Game
'''


gameMapString=[
  "##########################################################",
  "#      J #~~~~~~~~~    i      #    #i* #  J             <#",
  "# @  i   #~~~~~~~~####    $   =  i H<#        $  ^   <#  #",
  "#        #~~~~~~~#   #        #    #>       ^   <#>   v  #",
  "###H######      #  $ #  i     #    #       <#>   v ^     #",
  "#        =  i +#   $ #        #    #  ^     v     <#>    #",
  "#  i  *  #######     #>       #    #  #> ^    J    v     #",
  "##########    ###   ##       <#    #  v <#>     ^        #",
  "#       #     ~~~~~~~#   ##   #    #     v   ^ <#>  J    #",
  "#  |J|  #     ~~~~~~~#    v   #    #        <#> v        #",
  "#  |+|  =     ~~~~~             *  # J  ^ $  v          $#",
  "#       #     ~~~~~      ^         #   <#>       ^       #",
  "####################################    v       <#>     ^#",
  "#>        |*    $   <#      ~~~~~~~~#            v      ##",
  "#>        |*   $    <#     #~~~~~~~~ ##      ###      ## #",
  "#>        |*|*      <#    <#~~~~~~~~ +####         ###   #",
  "#>                   #>    #~~~~~~~~ +#   ####H####      #",
  "#>                   #    <#~~~~~~~~ ##      #H#       $ #",
  "#>                   #>    #~~~~~   #        v v    +    #",
  "#>                   #    <#~~~~~   #i#              $   #",
  "#>                   ##   #########H  #             +    #",
  "#>        |  ***     ## J #        H  #                  #",
  "#>                   ######         ######################",
  "#>                   #              #***                <#",
  "#>           ^^^^^^ $#              #**>                 #",
  "########### ##########              #***                <#",
  "#$=============      #      ##      ###################  #",
  "#==============#>       #>  $$  <#      <#       *     * #",
  "#==============      ################         *          #",
  "#H######### ##########   +       +  ######################",
  "#      #    #>> >>  v#             #>~~~~~~~~~~~~~~#  i  #",
  "###  ###v           v#   +    +   #>~~~~~~~~~~~~~~~#     #",
  "#vv  vv#v    *J*     #           #>~~~~~~~~~~#~~+~~##   ##",
  "#      #            v#   +  +   #>~~~~$~~~~~~#~~~~~### ###",
  "#      #>> >> >> >> v#         #>~~~~~~~~~~~~#~~~~~#~~~~~#",
  "###  ##################  +    #>~~~~~~~~~~~~~#~~~~~#~~~~~#",
  "#vv    #>            <#      #>~~~~~~~~~~~~~~#~~+~~#~~~~~#",
  "#                                 #~~~~+~~~~~#~~~~~~~~+~~#",
  "#>    <#>            <#           #~~~~~~~~~~#$~~~~~~~~~~#",
  "##########################################################",
]

def prinLegend():
  print("")
  print("Legend:")
  print("")
  print("# - hard wall, cannot destroy")
  print("| - same as #")
  print("@ - player")
  print("~ - water, can be traversed, but uses up health")
  print("  - air, can be traversed")
  print("> - glider")
  print("< - glider")
  print("v - glider")
  print("^ - glider")
  print("H - door, can only be opened with a key")
  print("= - wooden planks")
  print("+ - health")
  print("* - fire gem")
  print("$ - gold")
  print("J - key")
  print("i - tells you info, or changes stuff")
  print("")

autoActions=""

info=[]
info.append("There is a door bellow you, the key to it is at the right top corner of this room.\nGo get it, and get out of this room!")
info.append("Those are fire gems to the right, you can burn wood with them.\nThere are wooden planks blocking the exit, go and burn them!")
info.append("Here is some health potions (the \"+\") you'll need them to travel these water (the \"~\")\nGoing through the water worsens your health!")
info.append("Here is some gold. Take it!")
info.append("You see those sharp pointy things? They are called gliders.\nIf you get in their way they'll rip you to shreds!\nPass through these corridors and avoid them!")
info.append("You'll need a key here. BTW the gliders can not only shred you but wood too. Be careful, there is a glider waiting behind the door.")
info.append("Ok, listen... this looks bad, so I'll give you extended vision")
info.append("You need 2 keys here, why didn't you take all the keys while you where there? I'm taking away your extended vision!\nIf you did take all keys, good job!")
info.append("Here you are, at the end of this dungeon... You escaped!")

collectedInfo=False

gameMap=[]

traversableThings=[' ', '~']
breakableThings=['@', '=']
collectableThings=['$', 'J', '*', '+', 'i']
interactableThings=['=', 'H']

displayMessages=True
changeVision=True

player=(2, 2)
playerIsDead=False
playerWon=False
visibility=4

inventory={
  '$': 0,
  'J': 0,
  '*': 0,
  '+': 3.0,
  'i': 0
}

updatesGameMap=[]
for x in range(0, len(gameMapString[0])-1):
  updatesGameMap.append([])
  # updatesGameMap[x]=[]
  for y in range(0, len(gameMapString)-1):
    updatesGameMap[x].append(False)

def resetUpdatesMap():
  for x in range(0, len(gameMap)-1):
    for y in range(0, len(gameMap[0])-1):
      updatesGameMap[x][y]=False

def resetGame(how):
  global gameMap
  global gameMapString
  global player
  global playerIsDead
  global playerWon
  global visibility
  global inventory
  global displayMessages
  global changeVision
  
  if how=="normal":
    displayMessages=True
    changeVision=True
    visibility=4
  elif how=="auto":
    displayMessages=False
    changeVision=False
    visibility=8
  
  #set all game values
  player=(2, 2)
  playerIsDead=False
  playerWon=False

  inventory={
    '$': 0,
    'J': 0,
    '*': 0,
    '+': 3.0,
    'i': 0
  }

  #====> the 2 while loops <====
  #make the map into a 2d char array
  gameMap=[]
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
  

#allows to control what gets printed with only 1 variable
def printMsg(message):
  global displayMessages
  if displayMessages:
    print(message)


def didPlayerWin():
  return playerWon

def didPlayerDie():
  return playerIsDead

def getInventory():
  return inventory

def printBoard():
  global gameMap

  for y in range(max(0, player[1]-visibility), min(player[1]+visibility, len(gameMap[0]))):
    for x in range(max(0, player[0]-visibility), min(player[0]+visibility, len(gameMap))):
      print(gameMap[x][y], end="")
    print()


def contains(list, chosenElement):
  for element in list:
    if element==chosenElement:
      return True
  return False

  

def isTraversable(thing):
  global traversableThings
  return contains(traversableThings, thing)

def isBreakable(thing):
  global breakableThings
  return contains(breakableThings, thing)

def isCollectable(thing):
  global collectableThings
  return contains(collectableThings, thing)

def isInteractable(thing):
  global interactableThings
  return contains(interactableThings, thing)




def swap(coord1, coord2):
  temp=gameMap[coord1[0]][coord1[1]]
  gameMap[coord1[0]][coord1[1]]=gameMap[coord2[0]][coord2[1]]
  gameMap[coord2[0]][coord2[1]]=temp

  

def movePlayer(deltaX, deltaY):

  global gameMap
  global player
  global inventory
  global collectedInfo

  stuffInfront=gameMap[player[0]+deltaX][player[1]+deltaY]
  
  if isTraversable(stuffInfront):

    #remove health if water
    if gameMap[player[0]+deltaX][player[1]+deltaY]=='~':
      inventory['+']-=0.2;
      printMsg("You moved through \"~\" and lost 0.2 \"+\"")

      #if we lose, we lose
      if inventory['+']<=0:
        gameMap[player[0]][player[1]]=" "
        return

    #swap player and the thing we move into
    swap((player[0]+deltaX, player[1]+deltaY),
      (player[0], player[1]))

    #move the coordinates of the player
    player=(player[0]+deltaX, player[1]+deltaY)

  #if collectable, collect it and try to move the player again
  elif isCollectable(stuffInfront):

    #collecting info?
    if stuffInfront=='i':
        collectedInfo=True
    
    printMsg(f"You got 1 \"{stuffInfront}\"")
    inventory[stuffInfront]+=1
    gameMap[player[0]+deltaX][player[1]+deltaY]=" "
    
    movePlayer(deltaX, deltaY)

  #if burnable/openable, auto burn/open it if possible
  elif isInteractable(stuffInfront):
    if stuffInfront=='=':
      if inventory['*']>0:
        inventory['*']-=1
        printMsg("You burned a \"=\" lost a \"*\"")
        gameMap[player[0]+deltaX][player[1]+deltaY]=" "
    elif stuffInfront=='H':
      if inventory['J']>0:
        inventory['J']-=1
        printMsg("You opened a \"H\" and lost a \"J\"")
        gameMap[player[0]+deltaX][player[1]+deltaY]=" "
      


def updateGlider(x, y, dx, dy, altState):
  global updatesGameMap
  global gameMap
  
  #destroy if breakable
  if isBreakable(gameMap[x+dx][y+dy]):
    printMsg(f"{gameMap[x][y]} destroyed {gameMap[x+dx][y+dy]}")
    gameMap[x+dx][y+dy]=" "
    updatesGameMap[x+dx][y+dy]=True
    
  if isTraversable(gameMap[x+dx][y+dy]):
    swap((x, y), (x+dx, y+dy))
    updatesGameMap[x+dx][y+dy]=True
  else:
    gameMap[x][y]=altState

  updatesGameMap[x][y]=True

  
def updateGliders():
  global updatesGameMap
  
  for x in range(1, len(gameMap)-1):
    for y in range(1, len(gameMap[0])-1):
      if updatesGameMap[x][y]:
        continue

      if gameMap[x][y]=='>':
        updateGlider(x, y, 1, 0, '<')
      elif gameMap[x][y]=='<':
        updateGlider(x, y, -1, 0, '>')
      elif gameMap[x][y]=='^':
        updateGlider(x, y, 0, -1, 'v')
      elif gameMap[x][y]=='v':
        updateGlider(x, y, 0, 1, '^')

  resetUpdatesMap()
  
  
def updateMap():
  global playerIsDead
  global playerWon
  global info
  
  updateGliders()

  #have we died?
  if gameMap[player[0]][player[1]]!='@':
    playerIsDead=True
    return

  
  
  

def updatePlayerAndMap(dx, dy):
  global collectedInfo
  global inventory
  global visibility
  global playerWon
  
  movePlayer(dx, dy)
  updateMap()


  #manage which info to display
  if collectedInfo:
    collectedInfo=False

    printMsg("")
    printMsg(info[inventory['i']-1])
    printMsg("")

    
    if inventory['i']==7 and changeVision:
      visibility=8
    elif inventory['i']==8 and changeVision:
      visibility=4
    elif inventory['i']==9:
      playerWon=True
      return


