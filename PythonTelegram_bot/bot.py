from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters
from Commands.commands import CommandsMyBot

from config import TOKEN_MY_BOT
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename='bot.log',
    format = "%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8',
    filemode='a',
)


def register_handlers(app: Application):
    bot_commands = CommandsMyBot()
    list_commands_bot = [
        CommandHandler("start", bot_commands.start),
        CommandHandler("info", bot_commands.info),
        CommandHandler("available_commands", bot_commands.available_commands),
        CommandHandler("greeting", bot_commands.greeting),
        CommandHandler("echo", bot_commands.echo),
        CommandHandler("day_time", bot_commands.day_time),
        CommandHandler("info_about_system", bot_commands.info_about_system),
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

