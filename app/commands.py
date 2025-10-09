import asyncio
from abc import ABC, abstractmethod
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import time
from datetime import datetime
from pc_commands import *


class CommandsBot(ABC):
    @abstractmethod
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def greeting(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def day_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def author(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    #@abstractmethod
    #async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
       # pass

class CommandsMyBot(CommandsBot):
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Приветствую вас!\nЯ ваш персональный ассистент для оптимизации вашего пк, осуществления управления им с вашего разрешения")

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        commands_text = """
<b>Доступные команды:</b>
/start - Начало работы с ботом
/available_commands - выводит все доступные команды
/greeting - приветствие с юзером
/info - предоставляет информацию об этом боте
/day_time - выводит время, дату и день недели
/author - автор и создатель

<b>Кнопки для удобного взаимодействия с ботом:</b>
1. Команды - этот список
2. Инфа - о боте
3. Время - текущее время дата, день недели и год
4. Автор - об авторе

"""
    async def greeting(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = int(context.args[0])
        user = await context.bot.get_chat(user_id)
        if user:
            await update.message.reply_text(f"Приветствую вас {user}")
        else:
            return 'Юзера с таким id нет'

    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        info_bot = """Это мой первый тг бот для управления и оптимизации пк.
1. которого я хочу научить разговаривать
2. делать с моим компом то что я захочу
3. минимизировать затрату времени на обслуживание пк за счет автоматизации с помощью моего бота."""
        await update.message.reply_text(info_bot)

    async def day_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        monday_time = datetime.now()
        format_time = monday_time.strftime('%d.%m.%Y %H:%M')
        await update.message.reply_text(f'Сегодняшняя дата и время: {format_time}')

    async def author(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        INFO_ABOUT_AUTHOR = """Информация об авторе
фрик который решился на реализацию данного проекта зовут Саша(Shurik)
Да это я), мне 18 лет я начинающий пайтон разработчик.
это мой личный индивидуальный проект по созданию тг ботика для минимизации  затрат моего времени на оптимизацию пк, его процесс компонентов и тому подобных манипуляций
"""
        await update.message.reply_text(INFO_ABOUT_AUTHOR)
