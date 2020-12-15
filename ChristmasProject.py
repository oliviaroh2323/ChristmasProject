from microbit import *
from time import sleep
from random import choice
import random, music

# __________________
#
#     M E M O R Y
#      G A M E
# __________________
#
#     Olivia Roh
#    & Owen Smith
#   _____________
#
#     Dec. 2020
# __________________


## LED IMAGES

# happy face animation
def happyFaceA():
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "09990:"
                       "90009"))
    sleep(1)
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "99999:"
                       "00000"))
    sleep(0.1)
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "99099:"
                       "00900"))
    sleep(0.05)
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "90009:"
                       "09990"))
    sleep(1)

# sad face animation
def sadFaceA():
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "90009:"
                       "09990"))
    sleep(1)
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "00000:"
                       "99999"))
    sleep(0.1)
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "00900:"
                       "99099"))
    sleep(0.05)
    display.show(Image("00000:"
                       "09090:"
                       "00000:"
                       "09990:"
                       "90009"))
    sleep(1)

# circle
def circleS():
    music.play('circleM')
    display.show(Image("09990:"
                       "90009:"
                       "90009:"
                       "90009:"
                       "09990"))
    sleep(2)
    display.clear()

# square
def squareS():
    music.play('squareM')
    display.show(Image("99999:"
                       "90009:"
                       "90009:"
                       "90009:"
                       "99999"))
    sleep(2)
    display.clear()

# x
def xS():
    music.play('xM')
    display.show(Image("90009:"
                       "09090:"
                       "00900:"
                       "09090:"
                       "90009"))
    sleep(2)
    display.clear()

# ________________


## SOUND EFFECTS

# intro
introM = ["C4:1", "E4:1", "G4:1", "C5:3"]

# winner
winnerM = ["C4:1", "E4:1", "G4:1", "C5:2", "G4:1", "C5:3"]

# loser
loserM = ["C4:1", "C3:1", "C2:1", "C1:3"]

# next lvl
lvlM = ["C4:1", "E4:1", "G4:1"]

# circle
circleM = ["C4:3"]

# square
squareM = ["E4:3"]

# x
xM = ["G4:3"]

# ________________


## SET GAME

# store all patter shape in list
shapes1 = [circleS, squareS, xS]

# create list to store pattern and  usr input
pattern = []
guesses = []

# set round count
rndCounter = 0

# ________________


## GAME CODE

# show images
def show(rndCounter):
    """show random shapes and save to 'pattern'
    then allow user input"""
    guesses.clear()
    pattern.clear()
    for i in range(rndCounter):
        rndmchce = random.choice(shapes1)
        pattern.append(rndmchce)
        for f in pattern:
            f()
    usrInput()

# usr input
def usrInput():
    """show animation/sound depending on user input
    then compare user input with 'pattern'"""
    while len(guesses) != len(pattern):
        if pin1.is_touched():
            display.clear()
            circleS()
            guesses.append(circleS)
        elif pin2.is_touched():
            display.clear()
            squareS()
            guesses.append(squareS)
        elif pin1.is_touched and pin2.is_touched():
            display.clear()
            xS()
            guesses.append(xS)
    checkUsrGuess()

# check usr guess
def checkUsrGuess():
    """check if user input = 'pattern'
    if so, move onto next level
    if not, activate 'tooBad'"""
    if pattern == guesses:
        pass
    else:
        tooBad()

# fail
def tooBad():
    """shown when user response is incorrect"""
    music.play(loserM)
    display.scroll('Too Bad...')
    sadFaceA()
    display.clear()
    """restart"""
    sleep(2)
    intro()

# success
def youDidIt():
    """shown when user has completed all levels"""
    music.play(winnerM)
    display.scroll('You Did It!')
    happyFaceA()
    display.clear()
    """restart"""
    sleep(2)
    intro()

# levels
def levels(rndCounter):

    """game is divised into seven levels
    each round shows an amount of random patterns which grows each levels
    the user has to copy the pattern in order to win"""

    # lvl 1
    rndCounter += 1
    music.play(lvlM)
    display.scroll('Level 1')
    show(rndCounter)

    # lvl 2
    rndCounter += 1
    music.play(lvlM)
    display.scroll('Level 2')
    show(rndCounter)

    # lvl 3
    rndCounter += 1
    music.play(lvlM)
    display.scroll('Level 3')
    show(rndCounter)

    # lvl 4
    rndCounter += 1
    music.play(lvlM)
    display.scroll('Level 4')
    show(rndCounter)

    # lvl 5
    rndCounter += 1
    music.play(lvlM)
    display.scroll('Level 5')
    show(rndCounter)
    youDidIt()

# intro
def intro():
    """play intro music & show title"""
    music.play(introM)
    display.scroll('Memory Game')

    """start game when button a is pressed"""
    display.scroll('Press A to Start')
    while True:
        if button_a.is_pressed():
            levels(rndCounter)

# ________________


## RUN CODE

intro()

# ________________
