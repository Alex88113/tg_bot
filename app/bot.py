from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from commands import CommandsMyBot
from dotenv import load_dotenv
import logging
import os
from pc_commands import PcCommandsBot


# Загрузка переменных окружения
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

logging.basicConfig(
    filename = 'result_work_bot.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

pc_commands_bot = PcCommandsBot()
bot_commands = CommandsMyBot()
bot_app = Application.builder().token(TOKEN_MY_BOT).build()

print('Начало запуска скрипта')
logging.debug('Начало запуска бота')

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


async def command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Команда получена')


def main():
    bot_app = Application.builder().token(TOKEN_MY_BOT).build()
    all_commands = list_commands + list_pc_commands

    for command in all_commands:
        try:
            bot_app.add_handler(command)
            logging.info(f'Команда {command} - успешно добавлена!')
        except Exception as error:
            logging.error(f"Ошибка с {command}: {error}")

    # Запускаем бота
    bot_app.run_polling()


if __name__ == "__main__":
    main()