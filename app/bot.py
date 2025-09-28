from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters
from commands import CommandsMyBot
import os
import sys
from dotenv import load_dotenv
import logging

# Загрузка переменных окружения
load_dotenv()
TOKEN_MY_BOT = os.getenv("TOKEN_MY_BOT")

# Проверка наличия токена
if not TOKEN_MY_BOT:
    print("Ошибка: TOKEN_MY_BOT не найден в переменных окружения")
    sys.exit(1)

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)


file_handler = logging.FileHandler('/app/bot_bags.log')
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.debug("Скрипт запущен")

bot_commands = CommandsMyBot()

async def handle_all_text_message(update, context):
    """Обработчик всех текстовых сообщений"""
    try:
        user_text = update.message.text.strip().lower().capitalize()
        logger.debug(f"Получено сообщение от {update.message.from_user.id}: {user_text}")
        answered = await bot_commands.handle_text(update, context)
        if not answered:
            await update.message.reply_text(
                "Я не понял ваш запрос. Используйте кнопки или команды.",
                reply_markup=bot_commands.main_keyboard
            )
            logger.debug(f"Сообщение не обработано: {user_text}")
    except Exception as e:
        logger.error(f'Ошибка в обработке сообщения: {e}')
        await update.message("Произошла ошибка при обработке вашего сообщения")

def register_handlers(app: Application):
    """Регистрация всех обработчиков"""
    try:
        # Список команд бота
        list_commands_bot = [
            ("start", bot_commands.start),
            ("info", bot_commands.info),
            ("available_commands", bot_commands.available_commands),
            ("greeting", bot_commands.greeting),
            ("day_time", bot_commands.day_time),
            ("author", bot_commands.author),
        ]

        # Регистрируем команды
        for command, handler in list_commands_bot:
            app.add_handler(CommandHandler(command, handler))
            logger.debug(f"Команда /{command} успешно зарегистрирована.")

        # Регистрация обработчика текстовых сообщений
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_all_text_message))
        logger.debug("Обработчик текстовых сообщений успешно подключён.")

    except Exception as e:
        logger.error(f"Ошибка при регистрации обработчиков: {e}")
        raise


def main():
    """Основная функция запуска бота"""
    try:
        logger.info("Запуск бота... Инициализация Application.")

        # Создаем приложение с обработкой ошибок
        app: Application = ApplicationBuilder() \
            .token(TOKEN_MY_BOT) \
            .build()

        register_handlers(app)

        logger.info("Бот запущен и готов к работе")
        app.run_polling(
            drop_pending_updates=True,  # Игнорировать сообщения, отправленные когда бот был офлайн
            allowed_updates=["message", "edited_message", "callback_query"],
            close_loop=False
        )

    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")


if __name__ == "__main__":
    main()