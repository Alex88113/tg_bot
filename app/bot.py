from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from commands import CommandsMyBot
from dotenv import load_dotenv
import logging
import os
from pc_commands import PcCommandsBot
from pydantic import BaseModel

# Загрузка переменных окружения
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

if not TOKEN_MY_BOT:
    raise ValueError("Токен бота не найден")

logging.basicConfig(
    filename = 'result_work_bot.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class Config(BaseModel):
    token: str
    admin_id: int = 0



async def unknown_team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text
    await update.message.reply_text(f"Команда '{command}' не найдена")
    logging.info(f'Пользователь ввел неизвестную команду: {command}')


async def command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        pass
    except Exception as error:
        logging.error(f'error in: {error}')
        await update.message.reply_text("Произошла ошибка")


def main():
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

    all_commands = list_commands + list_pc_commands

    for command in all_commands:
        try:
            bot_app.add_handler(command)
            logging.info(f'Команда {command} - успешно добавлена!')
        except Exception as error:
            logging.error(f"Ошибка с: {error}")

    bot_app.add_handler(MessageHandler(filters.COMMAND, unknown_team))
    print('Добавлен обработчик неизвестных команд')

    print('Ботяра запускается.....')
    bot_app.run_polling()

if __name__ == "__main__":
    main()