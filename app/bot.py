from telegram.ext import Application, ApplicationBuilder, CommandHandler
from commands import CommandsMyBot
from dotenv import load_dotenv
import logging
import os
from pc_commands import PcCommandsBot

# Загрузка переменных окружения
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

pc_commands_bot = PcCommandsBot()
bot_commands = CommandsMyBot()
bot_app = Application.builder().token(TOKEN_MY_BOT).build()
print('Начало запуска скрипта')

list_commands = [
    CommandHandler('start', bot_commands.start),
    CommandHandler('help', bot_commands.help),
    CommandHandler('greeting', bot_commands.greeting),
    CommandHandler('info', bot_commands.info),
    CommandHandler('day_time', bot_commands.day_time),
    CommandHandler('author', bot_commands.author)
]

list_pc_commands = [
    CommandHandler('system_info', pc_commands_bot.system_info),
    CommandHandler('processor_info', pc_commands_bot.processor_info),
    CommandHandler('disk', pc_commands_bot.disk)
]

if __name__ == "__main__":
    for command in list_commands:
        bot_app.add_handler(command)

    for handler in list_pc_commands:
        bot_app.add_handler(handler)

    bot_app.run_polling()