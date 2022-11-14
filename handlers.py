# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    dp.register_message_handler(commands.new, commands=['new'])
    dp.register_message_handler(commands.settings, commands=['settings'])
    dp.register_message_handler(commands.setTotal, commands=['candy'])
    dp.register_message_handler(commands.setMax, commands=['max'])
    dp.register_message_handler(commands.setDifficulty, commands=['difficulty'])
    dp.register_message_handler(commands.cancelSettings, commands=['cancel'])
    dp.register_message_handler(commands.setLow, commands=['low'])
    dp.register_message_handler(commands.setHard, commands=['hard'])
    dp.register_message_handler(commands.getNumber)