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

  while True:
    choice = input("Type 2 to autoplay the game\nType 1 to start\nType 0 to quit\ninput: ")
  
    if choice == "1":
      print("Starting the game")
      main_loop_Menu()
    elif choice == "0":
      print("you choose to quit ")
      quit()
    else:
      print("invalid input")
    


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


