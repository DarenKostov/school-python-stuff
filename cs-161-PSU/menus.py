'''
Thierry Ndayisaba
Daren Kostov

Licence: GPLv3
https://www.gnu.org/licenses/gpl-3.0.en.html

This is part of the Escape Room Game
'''


from logic import *
from logic import inventory




def main_menu():
  print("welcome to our escape room Game!")
  choice = input("type 1 to start and 0 to quit: ")
  
  if choice == "1":
    print("Starting the game")
    main_loop_Menu()
  elif choice == "0":
    print("you choose to quit ")
    quit()
  else:
    print("invalid input")
    main_menu()


#nice, ill just replace the move function
#you know what the error is on movePlayer
#no idea
#it runs so it should be fine i think ...hmmmm
#i think it's ok
# im going to write the invitory menu
# fixed it!

#btw printBoard() prints the game map
# where 
#where to put? after collecting all of the inputs
#and changing the map
#aka at the end of each turn
# im kind confused 
#about what
#the map thing 
#its just where all of the walls, enemies, keys, etc are
'''
it looks like this at the moment
"#" are walls
"@" is player

"j" and "t" are nothing, just random chars to help me
make sure that the dirrections are correct

#####
# j #
# @t#
#   #
#####
'''
#okay i understand now thanks bro
# np

#I have an idea on how to handle the invalid input

#I think we have the foundation
#player can move and the menu works
# so like when is the player win like whats the output?
'''
======================
========YOU===========
==========WIN=========
======================

something like that ^^^

'''
# so should i add like if the player collects all of the keys it outpusts that
#sure, or goes to the final room, or beat the boss
#I havent actually thought about the main objective
#The player escapes rooms but what is his goal hmmm :/
# i think we should give them points or print how many tries they did to win
#ok, we can have like a validTurns variable that just keeps track of that, yeah
# for sure
# should i create new menu about it
#new function

def main_loop_Menu():
  
  printBoard()
  
  gameOver=False
  previousChoice="none"
  while not gameOver:
    validInput=True
    
    choice = input("click WASD keys to move: ").lower()
    
    if len(choice)==0:
      choice=previousChoice
      
    
    if choice == "w":
      movePlayer(0, -1)
    elif choice == "a":
      movePlayer(-1, 0)
    elif choice == "s":
      movePlayer(0, 1)
    elif choice == "d":
      movePlayer(1, 0)

      
      
    else:
      validInput=False


    if validInput:
      previousChoice=choice
      updateMap()
      printBoard()
    else:
      print("invalid input")

def invatory_menu():
  keys = 0
  print("you have collected the following keys: ")
  for item in inventory:
    print(item)
    keys += 1
  print("you have collected", keys, "keys")
  choice = input("type 1 to go back to the menu: ")
  if choice == "1":
    main_menu()
  else:
    print("invalid input")
    invatory_menu()


