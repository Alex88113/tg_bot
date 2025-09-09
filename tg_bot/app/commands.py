import asyncio

from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import ContextTypes, filters

import time
from telegram import ReplyKeyboardMarkup


class CommandsBot(ABC):
    @abstractmethod
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def available_commands(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def greeting(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        await update.message.reply_text("Я персональный голосовой ассистент для управления пк, с твоего разрешения.") # type: ignore

    async def available_commands(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("""
/start: Это дефолтная команда начала взаимодействия с ботом.
/available_commands: Выводит всю информацию об доступных командах
/greeting: Приветствие с юзером
/echo: Показывает текст который вы ввели
/info: Выводит информацию о моём ботe
/day_time: Представляет сегодняшную дату и время
/author: Автор и создатель этого детища!
""") # type: ignore
        
    async def greeting(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message:
            await update.message.reply_text(
                """Приветствую вас Александр!
чем могу помочь?:"""
            )

    async def echo(self, update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f"Текст который вы написали: {user_text}") # type: ignore

    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await asyncio.sleep(2)
        await update.message.reply_text( # type: ignore
            "Это мой первый личный помощник в тг, которого я научу говорить и управлять мои пк, при помощи моих войс команд")

    async def day_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await asyncio.sleep(2)
        todays_time = time.strftime('%H:%M')
        and_date = time.strftime("%d %B %A %Y")
        await update.message.reply_text(f"Сегодняшнее время и дата:\nВремя: {todays_time}\nДата: {and_date}") # pyright: ignore[reportOptionalMemberAccess]

        
    async def author(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        name_author = "Shura"
        processing_author_name= name_author.strip().lower().title()
        await update.message.reply_text(f"Ник создателя и автора этого детища -> {processing_author_name}")
