from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters
from commands import CommandsMyBot
import os

import sys

from dotenv import load_dotenv
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(ascitme)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('/app/bot_bags.log')
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logging.debug("Скрипт запущен")

print("Скрипт запущен")

def register_handlers(app: Application):
    bot_commands = CommandsMyBot()
    list_commands_bot = [
        CommandHandler("start", bot_commands.start),
        CommandHandler("info", bot_commands.info),
        CommandHandler("available_commands", bot_commands.available_commands),
        CommandHandler("greeting", bot_commands.greeting),
        CommandHandler("echo", bot_commands.echo),
        CommandHandler("day_time", bot_commands.day_time),
        CommandHandler("author", bot_commands.author)
    ]

    for command in list_commands_bot:
        app.add_handler(command)

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_commands.echo))


def main():
    logging.info("Запуск бота...Инициализация Application.")
    app: Application = ApplicationBuilder().token(TOKEN_MY_BOT).build()
    register_handlers(app)
    logging.info("Бот запущен")
    app.run_polling()



if __name__ == "__main__":
    main()

