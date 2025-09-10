from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters
from commands import CommandsMyBot
import os
import sys

from dotenv import load_dotenv
import asyncio

# Загрузка переменных окружения
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('/app/bot_bags.log')
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.debug("Скрипт запущен")  # Исправлено: используем logger вместо logging

print("Скрипт запущен")

async def handle_all_text_message(update, context):
    user_text = update.message.text
    bot_commands = CommandsMyBot()
    answered= await bot_commands.answer_question(update, context)
    if answered:
        return
    await update.message.reply_text(f"Вы напечатали: {user_text}")
    
def register_handlers(app: Application):
    bot_commands = CommandsMyBot()
    list_commands_bot = [
        ("start", bot_commands.start),  # Исправлено: кортежи (command, handler)
        ("info", bot_commands.info),
        ("available_commands", bot_commands.available_commands),
        ("greeting", bot_commands.greeting),
        #("echo", bot_commands.echo),
        ("day_time", bot_commands.day_time),
        ("author", bot_commands.author),
    ]

    for command, handler in list_commands_bot:
        try:
            app.add_handler(CommandHandler(command, handler))  # Исправлено: правильные параметры
            logger.debug(f"Команда /{command} успешно зарегана.")
        except Exception as e:
            logger.error(f"Ошибка в регистарции команд: {e}")
            
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_all_text_message))
    logger.debug("Обработчик текстовых сообщенний успешно подключён.")


def main():
    logger.info("Запуск бота...Инициализация Application.")  # Исправлено: используем logger вместо logging
    app: Application = ApplicationBuilder().token(TOKEN_MY_BOT).build()
    register_handlers(app)
    
    logger.info("Бот запущен")  # Исправлено: используем logger вместо logging
    app.run_polling()

if __name__ == "__main__":
    main()
