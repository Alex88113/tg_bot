from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from commands import CommandsMyBot
from dotenv import load_dotenv
import os
from loggers_commands import *
from pc_commands import PcCommandsBot


# Загрузка переменных окружения
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

if not TOKEN_MY_BOT:
    raise ValueError("Токен бота не найден")



async def unknown_team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text
    await update.message.reply_text(f"Команда '{command}' не найдена")
    error_logger.error(f'Пользователь ввел неизвестную команду: {command}')


async def command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        pass
    except Exception as error:
        error_logger.error(f'error in: {error}')
        await update.message.reply_text("Произошла ошибка")


def main():
    pc_commands_bot = PcCommandsBot()
    bot_commands = CommandsMyBot()
    bot_app = Application.builder().token(TOKEN_MY_BOT).build()

    print('Начало запуска скрипта')
    debug_logger.debug('Начало запуска бота')

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
        CommandHandler('disk', pc_commands_bot.disk),
        CommandHandler('users_system', pc_commands_bot.users_system),
        CommandHandler('access_memory', pc_commands_bot.access_memory),
        CommandHandler('time_start_system', pc_commands_bot.time_start_system)
    ]

    all_commands = list_commands + list_pc_commands

    for command in all_commands:
        try:
            bot_app.add_handler(command)
            result_logger.info(f'Команда {command} - успешно добавлена!\n')
        except Exception as error:
            error_logger.error(f"Ошибка с: {error}")
            
    debug_logger.debug('Добавлен обраточик неизвестных команд')
    bot_app.add_handler(MessageHandler(filters.COMMAND, unknown_team))
    print('Добавлен обработчик неизвестных команд')
    debug_logger.debug('Бот запустился\n')
    result_logger.info("Бот успешно запустился")
    print('Ботяра запускается.....')
    bot_app.run_polling()

if __name__ == "__main__":
    main()
