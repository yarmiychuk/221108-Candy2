# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view, model
from bot import bot

async def start(message: types.Message):
    model.noGame()
    await view.greetings(message, model.getStartTotal(), model.getCurrentMax())

async def new(message: types.Message):
    model.resetGame()
    await nextTurn(message)

async def finish(message: types.Message):
    await view.bye(message)

async def isNotInGame(message: types.Message):
    if (model.candies == 0):
        return True
    await view.endThisGame(message)
    return False

async def settings(message: types.Message):
    if await isNotInGame(message):
        await view.showSettings(message)

async def setTotal(message: types.Message):
    if await isNotInGame(message):
        model.activateSettings(model.SET_TOTAL)
        await view.changeTotal(message, model.getStartTotal())

async def setMax(message: types.Message):
    if await isNotInGame(message):
        model.activateSettings(model.SET_TURN)
        await view.changeMax(message, model.getCurrentMax(), model.getStartTotal())

async def setDifficulty(message: types.Message):
    if await isNotInGame(message):
        model.activateSettings(model.SET_DIFFICULTY)
        await view.changeDifficulty(message)

async def cancelSettings(message: types.Message):
    await resetSettings(message)

async def setLow(message: types.Message):
    if await isNotInGame(message):
        model.setDifficulty(model.LOW_DIFFICULTY)
        await resetSettings(message)

async def setHard(message: types.Message):
    if await isNotInGame(message):
        model.setDifficulty(model.HARD_DIFFICULTY)
        await resetSettings(message)

async def resetSettings(message: types.Message):
    model.resetSettings()
    await view.greetings(message, model.getStartTotal(), model.getCurrentMax())

async def getNumber(message: types.Message):
    input = message.text
    if input.isnumeric():
        count = int(input)
        if model.getCandies() > 0:
            await playerTurn(message, count)
        else:
            match model.getSettingsMode():
                case model.SET_TOTAL:
                    await setTotalCount(message, count)
                case model.SET_TURN:
                    await setMaxCount(message, count)

async def playerTurn(message: types.Message, count: int):
    if 0 < count <= model.getCurrentMax():
        model.playerTakes(int(count))
        await nextTurn(message)
    else:
        await view.сheater(message)

async def setTotalCount(message: types.Message, count: int):
    if model.MIN_CANDIES <= count <= model.MAX_CANDIES:
        model.setTotalCandies(count)
        await resetSettings(message)
    else:
        await view.сheater(message)

async def setMaxCount(message: types.Message, count: int):
    if 1 < count < model.getStartTotal():
        model.setMaxTurn(count)
        await resetSettings(message)
    else:
        await view.сheater(message)

async def nextTurn(message: types.Message):
    if model.candies > 0:
        model.changePlayer()
        if model.isPlayerTurn:
            await view.askPlayerTurn(message, model.candies, model.getMax())
        else:
            await view.botTurn(message, model.candies, model.botTakes())
            await nextTurn(message)
    else:
        await endGame(message)

async def endGame(message: types.Message):
    await view.endGame(message, model.isPlayerTurn)
    model.noGame()