'''
Thierry Ndayisaba
Daren Kostov

Licence: GPLv3
https://www.gnu.org/licenses/gpl-3.0.en.html

This is part of the Escape Room Game
'''


from logic import *
from time import sleep

winningRecord="dddddwssaaaasssssdddddwwdddddddwdwwwwdddddddddsssddwwdddssssssssdddssaaaaaaaaaaaaaaaaaaaaaaaaaaawaaaawwaasssdddwddddwwddddddwwwwddssssssddddds dddddddddddddwwwwwwwwwddwssddwddddsssaassssssdas   wddddddddswdddswdddddwwwwaaaaaaassaaaasaawawwwawaas    wwwwddsddwddss w    ssssssasssdssssddddsssssssaaaadsdddddddddwwwdddwssaassaaaaaaawwaaaaaaaawaasssaawaasssaaaaaaadddddsswwwwwddwwwwdwwdsasawdwaaaaaaawwaaasaaaas ssssssssdssddwwwwdwawwwddddddddddssssssessssssawwwaaaaaasaaaaasssdddwddddddddddssdaawwwdsssddsddddddddddddwdddddddwwaaaaaaawaawaaaaaaaaaaassddwaddddddssssssssssdddddddddddssaaaaaaaaaaaassaaaaaa          wwaawwaaaaaaaaaaaas ssaaasaaaaawwdwwaaaaaaaaawwwwwdda  ddddsawaaaasaaaaaaaawwwwwwwdsdddddddwwwsssddwwdaadddwdaaaaass    sssassdssssssssssssssdddddddaaaaaaawwwwwwwwaaaaawaddddddssssssaaaaaaaaaaaaaaaaaaaaswwwssssdddsssssssdddddddddddddddddddddwwwwwwwwddddddddsasaasssaawssaasassddddddddwwwwdddddwwwwdddddddwdsddsssssssaaddddddddwwwwwwww"

def main_menu():
  print("welcome to our escape room Game!")

  while True:
    choice = input("Type 3 to print the legend\nType 2 to autoplay the game\nType 1 to start\nType 0 to quit\ninput: ")
  
    if choice == "1":
      print("Starting the game")
      main_loop_Menu()
    elif choice == "2":
      print("Starting the game in auto mode")
      mainGameLoopAuto()
    elif choice == "3":
      prinLegend()
    elif choice == "0":
      print("you choose to quit ")
      quit()
    else:
      print("invalid input")
    

def playATurn(choice):
  dx=0
  dy=0
  
  if choice=="w":
    (dx, dy)=(0, -1)
  elif choice=="a":
    (dx, dy)=(-1, 0)
  elif choice=="s":
    (dx, dy)=(0, 1)
  elif choice=="d":
    (dx, dy)=(1, 0)
  elif choice=="e":
    printInventory()
  elif choice!=" ":
    print("invalid input")
    return False

  
  updatePlayerAndMap(dx, dy)
  printBoard()

  return True

def printHelp():
  print('You move by typing "w", "a", "s", and "d"')
  print('You can also check you inventory with "e", it takes a turn though')
  print('When you input a space no actions are take but you still play a turn')
  print('You can also input nothing and your last input will be takes instead')
  print('When you run into object you auto interact with them')
  print('Oh and btw make sure you collect the "i"\'s, they\'ll help you')
  print('Alright that\' all you need to know\n')
  print('("q" quits the game)')

  
def printWinOrLose():
  if didPlayerWin():
    print("/‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\")
    print("|==[O]==YOU======()==|")
    print("|=(:)=====WIN=={$}===|")
    print("\\____________________/")
    print()
    print(f"You got ${getInventory()['$']}/$16")
    print()
  else:
    print("                      ")
    print("        YOU           ")
    print("          LOSE        ")
    print("                      ")

def main_loop_Menu():

  
  resetGame("normal")
  
  printHelp()

  printBoard()
  
  previousChoice="none"
  #while the player has not yet won or lost run the loop
  while didPlayerDie()+didPlayerWin()==0:
    
    choice = input("Type WASD keys to move\nE to print inventory\nor Q to quit: ").lower()

    #in case we wanna quit the current game
    if choice=="q":
      print("are you sure you wanna quit?")
      choice=input('Type "yes": ')

      if choice=="yes":
        return
      else:
        continue

      
    #if we just press enter play the previous input
    if len(choice)==0:
      choice=previousChoice


    #if the input was valid, remember it
    if playATurn(choice):
      previousChoice=choice    
    
  printWinOrLose()

def mainGameLoopAuto():
  resetGame("auto")
  printBoard()

  for i in winningRecord:
    playATurn(i)
    sleep(0.1)
  printWinOrLose()


def printInventory():
  inventory=getInventory()

  
  print("\nYour inventoy: ")
  for item in inventory:
    print(f"{item} = {inventory[item]:0.1f}")
  print()


