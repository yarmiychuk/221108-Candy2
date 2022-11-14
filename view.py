# Сюда все функции отправляющие сообщения

from aiogram import types
from bot import bot

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, привет! Я хочу сыграть с тобой в одну игру...\n\n'
        f'Это игра в конфетки. На столе лежит 150 конфет. Мы будем брать конфеты по очереди, '
        f'но не более 28 штук за ход. Очередность первого хода определяется жеребьёвкой.\n'
        f'Победит тот, кто заберёт оставшиеся на столе конфеты последним.\n\n'
        f'/new - начать новую игру\n/finish - завершить игру')

async def сheater(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')

async def bye(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'До свидания!')

def getEndOfWord(count: int):
    if count > 100:
        count -= 100
    if count > 4 and count < 21:
        return ''
    c = count % 10
    if c > 4 or c == 0:
        return ''
    elif c == 1:
        return 'а'
    return 'ы'

async def askPlayerTurn(message: types.Message, count: int, maxGet: int):
    await bot.send_message(message.from_user.id,
        f'На столе {count} конфет{getEndOfWord(count)}.\nТвой ход! Сколько конфет ты возьмёшь (1-{maxGet})?')

async def botTurn(message: types.Message, count: int, get: int):
    await bot.send_message(message.from_user.id,
        f'Осталось {count} конфет{getEndOfWord(count)}.\nЯ забираю {get}.')

async def endGame(message: types.Message, isPlayerWin: bool):
    await bot.send_message(message.from_user.id,
        f'На столе не осталось конфет...')
    if isPlayerWin:
        await bot.send_message(message.from_user.id,
            f'Что же, ты победил меня, поздравляю. Если хочешь сыграть ещё раз, набери команду /new')
    else:
        await bot.send_message(message.from_user.id,
            f'Я победил тебя. Если хочешь сыграть ещё раз, набери команду /new')