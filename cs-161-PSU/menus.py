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
    elif choice == "2":
      print("Starting the game in auto mode")
      mainGameLoopAuto()
    elif choice == "0":
      print("you choose to quit ")
      quit()
    else:
      print("invalid input")
    

def playATurn(choice):
  dx=0
  dy=0
  
  if choice == "w":
    (dx, dy)=(0, -1)
  elif choice == "a":
    (dx, dy)=(-1, 0)
  elif choice == "s":
    (dx, dy)=(0, 1)
  elif choice == "d":
    (dx, dy)=(1, 0)
  elif choice== "e":
    printInventory()
  else:
    print("invalid input")
    return False

  
  updatePlayerAndMap(dx, dy)
  printBoard()

  return True



def main_loop_Menu():
  global playerIsDead
  global playerWon
  resetGame()
  
  printBoard()
  
  previousChoice="none"
  #while the player has not yet won or lost run the loop
  while playerIsDead+playerWon==0:
    
    choice = input("click WASD keys to move\nor E to print inventory: ").lower()

    #if we just press enter play the previous input
    if len(choice)==0:
      choice=previousChoice


    #if the input was valid, remember it
    if playATurn(choice):
      previousChoice=choice    
    
  if playerWon:
    print("/‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\")
    print("|==[O]==YOU======()==|")
    print("|=(:)=====WIN=={$}===|")
    print("\\____________________/")
  else:
    print("                      ")
    print("        YOU           ")
    print("          LOSE        ")
    print("                      ")







def printInvetory():

  print("Your inventoy: ")
  for item in inventory:
    print(f"{item} = {inventory[item]}")
  print()


