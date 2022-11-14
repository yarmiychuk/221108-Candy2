# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)

from random import randint as r

PLAYER_TURN = 0
SET_NONE = 0
SET_TOTAL = 1
SET_TURN = 2
SET_DIFFICULTY = 3
LOW_DIFFICULTY = 0
HARD_DIFFICULTY = 1
DEF_CANDIES = 150
MIN_CANDIES = 50
MAX_CANDIES = 500
DEF_MAX = 28

settings: int = SET_NONE
difficulty: int = LOW_DIFFICULTY
totalCandies = DEF_CANDIES
maxTurn: int = DEF_MAX
candies: int = 0
isPlayerTurn: bool = None

def resetGame():
    global candies, isPlayerTurn, settings
    candies = totalCandies
    isPlayerTurn = None
    settings = SET_NONE

def changePlayer():
    global isPlayerTurn
    isPlayerTurn = r(0, 1) == PLAYER_TURN if isPlayerTurn == None else not isPlayerTurn
    return isPlayerTurn

def getMax():
    global candies, maxTurn
    maxGet = candies if candies <= maxTurn else maxTurn
    return maxGet

def getCandies():
    global candies
    return candies

def botTakes():
    global candies, maxTurn
    if candies == totalCandies:
        howToGet = r(1, maxTurn)
        candies -= howToGet
        return howToGet
    howToGet = candies
    if candies > maxTurn:
        howToGet = (candies - 1) % maxTurn
        if howToGet == 0 or difficulty == LOW_DIFFICULTY:
            howToGet = r(1, maxTurn)
    candies -= howToGet
    return howToGet

def playerTakes(count: int):
    global candies
    candies -= count

def noGame():
    global candies, isPlayerTurn
    candies = 0
    isPlayerTurn = None

def setMaxTurn(count: int):
    global maxTurn, settings
    maxTurn = count
    settings = SET_NONE

def setTotalCandies(count: int):
    global totalCandies, settings
    totalCandies = count
    settings = SET_NONE

def setDifficulty(newDifficulty: int):
    global difficulty, settings
    difficulty = newDifficulty
    settings = SET_NONE

def resetSettings():
    global settings
    settings = SET_NONE

def activateSettings(setMode: int):
    global settings
    settings = setMode

def getSettingsMode():
    global settings
    return settings

def getStartTotal():
    global totalCandies
    return totalCandies

def getCurrentMax():
    global maxTurn
    return maxTurn

    