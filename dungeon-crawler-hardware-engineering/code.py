from random import randint
import numpy as np
from time import sleep
import sys
print (sys.version)


'''
Daren Kostov
5/1/2022
name: "Random dungeon crawler on the terminal"
Licence: GPL3
'''

swords={
    0:"None",
    1:"Stick",
    2:"Broad Sword",
    3:"Heavy Sword",
    4:"Sacred Blade"
}

def startup():
    #player coordinates
    global myX
    myX=1
    global myY
    myY=1
    
    #variable name is ourCoins since coins is used later
    global ourCoins
    ourCoins=0
    
    #variable that records our previuos action
    global previousAction
    previousAction=""
    
    #what melee weapon we currently have (also the damage of that weapon)
    global swordInHand
    swordInHand=0
    
    #variable name is ourKeys since key is used later
    global ourKeys
    ourKeys=0
    
    #global time
    global time
    time=0
    
    #the map of the game
    global terrain
    terrain=[
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2],
    [2 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,18,20,20,2 ,0 ,0 ,0 ,7 ,0 ,0 ,5 ,2 ,22,8 ,8 ,8 ,8 ,22,2],
    [2 ,0 ,0 ,2 ,2 ,2 ,2 ,2 ,4 ,0 ,0 ,2 ,3 ,2 ,20,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,8 ,8 ,8 ,8 ,8 ,8 ,2],
    [2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,8 ,8 ,15,15,8 ,8 ,2],
    [2 ,16,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,0 ,2 ,8 ,9 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,20,8 ,8 ,15,15,8 ,8 ,2],
    [2 ,4 ,0 ,0 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,8 ,8 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,8 ,8 ,8 ,8 ,8 ,8 ,2],
    [2 ,0 ,0 ,0 ,2 ,0 ,0 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,22,8 ,8 ,8 ,8 ,22,2],
    [2 ,0 ,0 ,0 ,7 ,0 ,2 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,2 ,0 ,0 ,0 ,2 ,0 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2],
    [2 ,0 ,0 ,0 ,0 ,0 ,2 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,2 ,0 ,0 ,0 ,2 ,3 ,2 ,2 ,21,0 ,0 ,0 ,0 ,0 ,0 ,21,2],
    [2 ,0 ,0 ,0 ,0 ,5 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,2 ,4 ,0 ,0 ,9 ,2 ,0 ,2 ,0 ,21,0 ,0 ,0 ,0 ,21,0 ,2],
    [2 ,4 ,7 ,0 ,0 ,0 ,2 ,7 ,7 ,7 ,7 ,7 ,2 ,20,2 ,0 ,0 ,2 ,2 ,3 ,2 ,0 ,0 ,0 ,21,0 ,0 ,21,0 ,0 ,2],
    [2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,17,2 ,0 ,0 ,0 ,2 ,0 ,2 ,2 ,0 ,0 ,0 ,15,15,0 ,0 ,0 ,2],
    [2 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,15,15,0 ,0 ,0 ,2],
    [2 ,6 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,15,15,0 ,0 ,0 ,2],
    [2 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,2 ,2 ,0 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,10,0 ,0 ,0 ,15,15,0 ,0 ,0 ,2],
    [2 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,2 ,3 ,3 ,2 ,0 ,0 ,0 ,0 ,6 ,0 ,2 ,0 ,0 ,21,0 ,0 ,21,0 ,0 ,2],
    [2 ,0 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,20,2 ,2 ,10,2 ,2 ,2 ,2 ,2 ,2 ,0 ,21,0 ,0 ,0 ,0 ,21,0 ,2],
    [2 ,6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,2 ,20,20,20,20,20,19,2 ,21,0 ,0 ,0 ,0 ,0 ,0 ,21,2],
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2]
    ]
    #transpose the terrain array since its not correctly set up by our method of rendering it
    terrain=np.transpose(terrain)
    
    #variable that tells us weather the cell has already been updated
    global isNotUpdated
    isNotUpdated=np.full((31,19),1)
startup()


#the manual
def manual():
    print(" : air")
    print("~: water")

    print("@: player")
    
    print("#: wall")
    print("%: paywall")
    print("=:locked door")

    print("$: coin")
    print("&: key")
    
    print(">: right glider")
    print("<: left glider")
    print("^: up glider")
    print("v: down glider")
    print("+: random glider")
    print("x: water random glider")
    
    
    print(".:boss health 1")
    print("::boss health 2")
    print("|:boss health 3")
    print("Y:boss health 4")
    print("X:boss health 5")
    
    print("/: stick")
    print("\\: broad sword")
    print("l: heavy sword")
    print("J: sacred blade")
    
    print("type w, a, s, or d and the enter to move")
    print("type e and then enter to see your inventory")
    print("type m and then enter to see this manual")
    
    print("Your goal is to defeat all bosses. Their aperease may be ., :, |, Y, or X.")
    print("You should also avoid gliders. Their aperease may be .>, <, ^, v, +, or x")
    print("Good luck!")
    print("oh and also pressing enter repeats your previous action")
    print("Good luck again!")

print("Welcome to Random dungeon crawler on the terminal!")
manual()
def air(x,y):
    return

def player(x,y):
    return

def wall(x,y):
    return

def coins(x,y):
    return

def right_glider(x,y):
    #if the next position is empty move there if not turn arround
    if(terrain[x+1][y]==0):
        terrain[x][y]=0
        terrain[x+1][y]=4
        isNotUpdated[x+1][y]=0
    else:
        terrain[x][y]=5

def left_glider(x,y):
    #if the next position is empty move there if not turn arround
    if(terrain[x-1][y]==0):
        terrain[x][y]=0
        terrain[x-1][y]=5
        isNotUpdated[x-1][y]=0
    else:
        terrain[x][y]=4
        
def up_glider(x,y):
    #if the next position is empty move there if not turn arround
    if(terrain[x][y-1]==0):
        terrain[x][y]=0
        terrain[x][y-1]=6
        isNotUpdated[x][y-1]=0
    else:
        terrain[x][y]=7
        
def down_glider(x,y):
    #if the next position is empty move there if not turn arround
    if(terrain[x][y+1]==0):
        terrain[x][y]=0
        terrain[x][y+1]=7
        isNotUpdated[x][y+1]=0
    else:
        terrain[x][y]=6
def water(x,y):
    return
def key(x,y):
    return
def door(x,y):
    return
#if 3 cycles of the global time have passed increase the stage of the boss cell
def boss1(x,y):
    if(time%3==0):
        terrain[x][y]=12
    return
def boss2(x,y):
    if(time%3==0):
        terrain[x][y]=13
    return
def boss3(x,y):
    if(time%3==0):
        terrain[x][y]=14
    return
def boss4(x,y):
    if(time%3==0):
        terrain[x][y]=15
    return

def boss5(x,y):
    return
def stick(x,y):
    return
def broadSword(x,y):
    return
def heavySword(x,y):
    return
def sacred_sword(x,y):
    return
def paywall(x,y):
    return
def random_glider(x,y):
    dirX=randint(-1,1)
    dirY=randint(-1,1)
    #if the next position is empty move there if not stay in one place
    if(terrain[x+dirX][y+dirY]==0):
        terrain[x][y]=0
        terrain[x+dirX][y+dirY]=21
        isNotUpdated[x+dirX][y+dirY]=0
        
def water_random_glider(x,y):
    dirX=randint(-1,1)
    dirY=randint(-1,1)
    #if the next position is water move there if not stay in one place
    if(terrain[x+dirX][y+dirY]==8):
        terrain[x][y]=8
        terrain[x+dirX][y+dirY]=22
        isNotUpdated[x+dirX][y+dirY]=0
        
#all cell operations so we can easily call them
operations=[air, player, wall, coins, right_glider, left_glider, up_glider, down_glider, water, key, door, boss1, boss2, boss3, boss4, boss5, stick, broadSword, heavySword, sacred_sword, paywall, random_glider, water_random_glider]
    
'''    
0: air
1: player
2: wall
3: coin
4: right glider
5: left glider
6: up glider
7: down glider
8: water
9: key
10:locked door

11:boss health 1
12:boss health 2
13:boss health 3
14:boss health 4
15:boss health 5

16: stick
17: broad sword
18: heavy sword
19: sacred blade
20: paywall
21: random glider
22: water random glider
'''

#all of the character that represent a cell
#            0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20    21   22
characters=[" ", "@", "#", "$", ">", "<", "^", "v", "~", "&", "=", ".", ":", "|", "Y", "X", "/", "\\", "l", "J", "%", "+", "x"]

def renderTerrain():
    #renders the terrain we can see, with "min+max magic" to avoid situations where we try to draw cells out of the array
    for y in range(max(0,min(19,myY-5)), max(0,min(19,myY+5))):
        row=""
        for x in range(max(0,min(31,myX-5)), max(0,min(31,myX+5))):
            row+=characters[terrain[x][y]]
        print(row)

renderTerrain()

while True:
    #our input that tells us we can type w, a, s, d, e, or m
    theInput=input("WASDEM:")
    #increase global time
    time+=1
    #set delta coordinates for our character
    dX=0
    dY=0
    
    #remeber our previous action that you can repeat by just pressing enter
    if theInput!="":
        previousAction=theInput
        
    #movement
    if previousAction=="w":
        dY=-1
    if previousAction=="a":
        dX=-1
    if previousAction=="s":
        dY=1
    if previousAction=="d":
        dX=1
    #inventory, dont count that as a move
    if theInput=="e":
        print("Coins:",ourCoins)
        print("Keys:",ourKeys)
        print("Weapon in hand:",swords[swordInHand])
        renderTerrain()
        continue
    #manual, dont count that as a move
    if theInput=="m":
        manual()
        renderTerrain()
        continue
        
        
    #remove our character to allow for easy collision implementation
    terrain[myX][myY]=0

    
    for y in range(19):
        for x in range(31):
            #if the cell was not updated update it and at the end make all cells non-updated
            if(isNotUpdated[x][y]):
                operations[terrain[x][y]](x,y)
    isNotUpdated[:]=1
    
    #in case of contact of...
    case=terrain[myX+dX][myY+dY]
    #in case of air, move
    if(case==0):
        myX+=dX
        myY+=dY
    #in case of glider you lose
    elif((case>3 and case<8) or case==21 or case==22):
        print("=========================")
        print("        you died")
        print("=========================")
        startup()
    #in case of water you move every 2 moves
    elif(case==8 and time%2==0):
        terrain[myX][myY]=8
        myX+=dX
        myY+=dY
    #in case of coins you can 1 coin
    elif(case==3):
        ourCoins+=1
        print(ourCoins)
        myX+=dX
        myY+=dY
    #in case of a key you get one key
    elif(case==9):
        ourKeys+=1
        myX+=dX
        myY+=dY
    #in case of a weapon you get the weapon (if its better than the one you have)
    elif(case>15 and case<20):
        swordInHand=max(swordInHand, case-15)
        myX+=dX
        myY+=dY
    #in case of the boss you remove health by bringing it to a weaker "state"
    elif(case>10 and case<16):
        terrain[myX+dX][myY+dY]-=swordInHand
        #if defeated give 1 coin
        if(terrain[myX+dX][myY+dY]<11):
            terrain[myX+dX][myY+dY]=0
            ourCoins+=1
    #in case of paywall and we have money we pass and lose 1 coin
    elif(case==20 and ourCoins>0):
        myX+=dX
        myY+=dY
        ourCoins-=1
    #in case of a locked door and we have keys we pass and lose 1 key
    elif(case==10 and ourKeys>0):
        myX+=dX
        myY+=dY
        ourKeys-=1
        


    #ugly if statemnt chain that check if all bosses are defeated
    if(terrain[26][3] not in range(11, 16)):
        if(terrain[27][3] not in range(11, 16)):
            if(terrain[26][4] not in range(11, 16)):
                if(terrain[27][4] not in range(11, 16)):
                    if(terrain[25][11] not in range(11, 16)):
                        if(terrain[26][11] not in range(11, 16)):
                            if(terrain[25][12] not in range(11, 16)):
                                if(terrain[26][12] not in range(11, 16)):
                                    if(terrain[25][13] not in range(11, 16)):
                                        if(terrain[26][13] not in range(11, 16)):
                                            if(terrain[25][14] not in range(11, 16)):
                                                if(terrain[26][14] not in range(11, 16)):
                                                    while True:
                                                        print("=========================")
                                                        print("        YOU WON!")
                                                        print("=========================")
                                                        print("        CONGRATS!")
                                                        print("=========================")
                                                        print("        YOU DID IT!") 
                                                        sleep(1)
    #return our character with updated coordinates
    terrain[myX][myY]=1
    #print our coordinates for debuging
    #print(myX,myY)
    #render our surroundings
    renderTerrain()
