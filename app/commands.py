import asyncio
from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import ContextTypes
import time
from datetime import datetime


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


class CommandsMyBot(CommandsBot):
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Приветствую вас!\nЯ ваш персональный ассистент для оптимизации вашего пк, осуществления управления им с вашего разрешения")

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text( """
Доступные команды:
/start - Начало работы с ботом
/help - выводит все доступные команды
/greeting - приветствие с юзером
/info - предоставляет информацию об этом боте
/day_time - выводит время, дату и день недели
/author - автор и создатель
=====Системные команды=====
/system_info - выводит ос систему пк и его архитектуру
/procerror_info - предоставляет большую часть информации об вашем процессоре вашего пк
/disk - эта команда показывает всё об вашем диске:
файловую систему, опции, количество свободного места ни диске, также и занятого пространства
/users_system - показывает ник текущего юзера в компьютере
/access_memory - выводит важную информацию об оперативной памяти
/time_start_system - предоставляет время запуска вашего компа""")

    async def greeting(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user
        if user_id:
            await update.message.reply_text(f"Приветствую вас {user_id.first_name}! Твой ID: {user_id}")
        else:
            await update.message.reply_text('Не удалось получить информацию о пользователя')

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
        await update.message.reply_text("""Информация об авторе
фрик который решился на реализацию данного проекта зовут Саша(Shurik)
Да это я), мне 18 лет я начинающий пайтон разработчик.
это мой личный индивидуальный проект по созданию тг ботика для минимизации  затрат моего времени на оптимизацию пк, его процесс компонентов и тому подобных манипуляций
""")
