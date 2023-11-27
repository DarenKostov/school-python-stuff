'''
Daren Kostov
Thierry Ndayisaba

Licence: GPLv3
https://www.gnu.org/licenses/gpl-3.0.en.html

This is part of the Escape Room Game
'''


#WIP game map
gameMapString=[
  "##########################################################",
  "#      J #~~~~~~~~~    i      #    #   #  J             <#",
  "# @  i   #~~~~~~~~####    $   =  i H<#           ^   <#  #",
  "#        #~~~~~~~#   #        #    #>       ^   <#>   v  #",
  "###H######      #  $ #  i     #    #       <#>   v ^     #",
  "#        =  i +#   $ #        #    #  ^     v     <#>    #",
  "#  i  ** #######     #>       #    #  #> ^    J    v     #",
  "##########    ###   ##       <#    #  v <#>     ^        #",
  "#       #     ~~~~~~~#   ##   #    #     v   ^ <#>  J    #",
  "#  |J|  #     ~~~~~~~#    v   #    #        <#> v        #",
  "#  |+|  =     ~~~~~                # J  ^    v           #",
  "#       #     ~~~~~      ^         #   <#>       ^       #",
  "####################################    v       <#>      #",
  "#>        |*        <#      ~~~~~~~~#            v      ##",
  "#>        |*        <#     #~~~~~~~~ ##      ###      ## #",
  "#>        |*|*      <#    <#~~~~~~~~ +####         ###   #",
  "#>                   #>    #~~~~~~~~ +#   ####H####      #",
  "#>                   #    <#~~~~~~~~ ##      #H#       $ #",
  "#>                   #>    #~~~~~   #        v v    +    #",
  "#>                   #    <#~~~~~   #i#              $   #",
  "#>                   ##   #########H  #             +    #",
  "#>        |  ***     ## J #        H  #                  #",
  "#>                   ######         ######################",
  "#>                   #              #***                <#",
  "#>           ^^^^^^  #              #**>                 #",
  "########### ##########              #***                <#",
  "#==============      #      ##      ###################  #",
  "#==============#>       #>  $$  <#      <#       *     * #",
  "#==============      ################         *          #",
  "#H######### ##########   +       +  ######################",
  "#      #    #>> >>  v#             #>~~~~~~~~~~~~~~#  i  #",
  "###  ###v           v#   +    +   #>~~~~~~~~~~~~~~~#     #",
  "#vv  vv#v    *J*     #           #>~~~~~~~~~~#~~+~~##   ##",
  "#      #            v#   +  +   #>~~~~~~~~~~~#~~~~~### ###",
  "#      #>> >> >> >> v#         #>~~~~~~~~~~~~#~~~~~#~~~~~#",
  "###  ##################  +    #>~~~~~~~~~~~~~#~~~~~#~~~~~#",
  "#vv    #>            <#      #>~~~~~~~~~~~~~~#~~+~~#~~~~~#",
  "#                                 #~~~~+~~~~~#~~~~~~~~+~~#",
  "#>    <#>            <#           #~~~~~~~~~~#~~~~~~~~~~~#",
  "##########################################################",
]


'''
Legend:

# - hard wall, cannot destroy
| - same as #
@ - player
~ - water, can be traversed, but uses up health
  - air, can be traversed
> - glider
< - glider
v - glider
^ - glider
H - door can only be opened with a key
= - wooden planks
+ - health
* - fire gem
$ - gold
J - key
i - tells you info, or changes stuff

'''



gameMap=[]

traversableThings=[' ', '~']
breakableThings=['@', '=']
collectableThings=['$', 'J', '*', '+', 'i']
burnableThings=['=', '+']


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

def isBurnable(thing):
  global burnableThings
  return contains(burnableThings, thing)




def swap(coord1, coord2):
  temp=gameMap[coord1[0]][coord1[1]]
  gameMap[coord1[0]][coord1[1]]=gameMap[coord2[0]][coord2[1]]
  gameMap[coord2[0]][coord2[1]]=temp

  

def movePlayer(deltaX, deltaY):

  global gameMap
  global player

  stuffInfront=gameMap[player[0]+deltaX][player[1]+deltaY]
  
  if isTraversable(stuffInfront):

    #remove health if water
    if gameMap[player[0]+deltaX][player[1]+deltaY]=='~':
      inventory['+']-=0.2;

      #if we loose, we loose
      if inventory['+']<=0:
        gameMap[player[0]][player[1]]=" "
        return

    #swap player and the thing we move into
    swap((player[0]+deltaX, player[1]+deltaY),
      (player[0], player[1]))

    #move the coordinates of the player
    player=(player[0]+deltaX, player[1]+deltaY)
  elif isTraversable(stuffInfront):


def updateGlider(x, y, dx, dy, altState):
  if isTraversable(gameMap[x+dx][y+dy]):
    swap((x, y), (x+dx, y+dy))
  else:
    gameMap[x][y]=altState

  
def updateGliders():
  for x in range(1, len(gameMap)-1):
    for y in range(1, len(gameMap[0])-1):
      if gameMap[x][y]=='>':
        updateGlider(x, y, 1, 0, '<')
      elif gameMap[x][y]=='<':
        updateGlider(x, y, -1, 0, '>')
      elif gameMap[x][y]=='^':
        updateGlider(x, y, 0, -1, 'v')
      elif gameMap[x][y]=='v':
        updateGlider(x, y, 0, 1, '^')
        
  
  

def updateMap():
  updateGliders()
  

printBoard()


