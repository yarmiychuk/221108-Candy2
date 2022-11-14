# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view, model
from bot import bot

async def start(message: types.Message):
    model.noGame()
    await view.greetings(message)

async def new(message: types.Message):
    model.resetGame()
    await nextTurn(message)

async def finish(message: types.Message):
    await view.bye(message)

async def getNumber(message: types.Message):
    input = message.text
    if input.isnumeric() and model.candies > 0:
        count = int(input)
        if 0 < int(count) < 29:
            model.playerTakes(int(count))
            await nextTurn(message)
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