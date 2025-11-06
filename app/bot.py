from telegram.ext import CommandHandler, ApplicationBuilder, MessageHandler, filters, Application, ContextTypes
from telegram import Update
import os
import asyncio
from dotenv import load_dotenv
from PcCommandsMonitoring.commands import *
from PcCommandsMonitoring.pc_commands import *
from PcCommandsMonitoring.loggers_commands import *

load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

if not TOKEN_MY_BOT:
    raise ValueError("Токен бота не найден")

debug_logger.debug('Запуск точки входа')
async def main():
    pc_commands_bot = PcCommandsBot()
    bot_commands = CommandsMyBot()
    application = ApplicationBuilder().token(TOKEN_MY_BOT).build()

    list_commands = {
        'start': bot_commands.start,
        'help': bot_commands.help,
        'greeting': bot_commands.greeting,
        'info': bot_commands.info,
        'day_time': bot_commands.day_time,
        'author': bot_commands.author
    }

    list_pc_commands = {
        'processor': pc_commands_bot.processor_info,
        'system_info': pc_commands_bot.system_info,
        'disk': pc_commands_bot.disk,
        'access_memory': pc_commands_bot.access_memory,
        'network': pc_commands_bot.collecting_network_statistics
    }
    result = list_commands | list_pc_commands
    debug_logger.debug('Производится регистрация команд')
    await asyncio.sleep(1)


    print("Начало регистрации команд")
    for name_command, command_function in result.items():
        application.add_handler(CommandHandler(name_command, command_function))
        result_logger.info(f'Зарегистрирована команда: {name_command}\n====================================================')
=======
    list_pc_commands = [
        CommandHandler('system_info', pc_commands_bot.system_info),
        CommandHandler('processor_info', pc_commands_bot.processor_info),
        CommandHandler('disk', pc_commands_bot.disk),
        CommandHandler('access_memory', pc_commands_bot.access_memory)
    ]


    debug_logger.debug('Обработчик обычных и системных команд  добавлен')
    print('Добавлен обработчик всех команд')

    try:
        await application.initialize()
        await application.start()
        await application.updater.start_polling()

        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt as error:
        error_logger.error(f'Причина остановки бота: {error}')
        print(f'Остановка бота... причина: {error}')
    finally:
        await application.updater.stop()
        await application.stop()
        await application.shutdown()

if __name__ == '__main__':
    print('Бот успешно запущен!')
    asyncio.run(main())
