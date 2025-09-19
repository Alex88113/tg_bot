import asyncio
from abc import ABC, abstractmethod
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import time
from datetime import datetime


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
    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def day_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def author(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

    @abstractmethod
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

class CommandsMyBot(CommandsBot):
    def __init__(self) -> None:
        self.main_keyboard = ReplyKeyboardMarkup(
            [
                ['Команды', 'Инфа'],
                ['Время', 'Автор'],
                ['Задать вопрос', 'Имена котиков'],
                ['Скрыть кнопки']
            ],
            resize_keyboard=True,
            input_field_placeholder="Выберите действие"
        )

        self.questions_keyboard = ReplyKeyboardMarkup(
            [
                ['Сколько времени?', 'Доступные команды'],
                ['Имена моих котиков', 'Назад']
            ],
            resize_keyboard=True
        )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_text = (
            "Я твой персональный ассистент для управления твоим ПК!\n\n"
            "Используй кнопки ниже для взаимодействия со мной:"
        )
        await update.message.reply_text(
            welcome_text,
            reply_markup=self.main_keyboard
        )

    async def available_commands(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
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
5. Задать вопрос - меню вопросов
6. Имена котиков - показать имена котиков
7. Скрыть кнопки - убрать клавиатуру"""

        await update.message.reply_text(
            commands_text,
            parse_mode='HTML',
            reply_markup=self.main_keyboard
        )

    async def greeting(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Приветствую вас, чем могу помочь?",
            reply_markup=self.main_keyboard
        )

    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await asyncio.sleep(2)
        info_text = """
<b>Информация о боте:</b>
Это мой первый личный помощник Телеграмм, которого я научу:
1. Отвечать на мои команды и вопросы
2. Управлять мои пк при помощи моего голоса
3. Разговаривать
4. Автоматизировать повседневные задачи
"""
        await update.message.reply_text(
            info_text,
            parse_mode='HTML',
            reply_markup=self.main_keyboard
        )

    async def day_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await asyncio.sleep(1)
        today_time = time.strftime('%H:%M')
        and_date = time.strftime("%d %B %A %Y")

        time_text = f"""
<b>Текущее время:</b>
Время: <code>{today_time}</code>
Дата: <code>{and_date}</code>
"""
        await update.message.reply_text(
            time_text,
            parse_mode="HTML",
            reply_markup=self.main_keyboard
        )

    async def author(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        name_author = "Shura"
        processing_author_name = name_author.strip().lower().title()
        author_info = f"""
<b>Информацию об авторе: </b>
Создатель: <code>{processing_author_name}</code>
Навыки: Python, Telegram Bot API
Цель: Научится создавать собственных персональных ассистентов
Статус: В стадии активной разработки"""

        await update.message.reply_text(
            author_info,
            parse_mode='HTML',
            reply_markup=self.main_keyboard
        )

    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        user_text = update.message.text
        user_text_clean = user_text.lower().strip().capitalize()
        print(f"DEBUG: Получен текст: '{user_text}' -> {user_text_clean}'")

        if 'Как зовут моих двух котиков?' in user_text_clean or 'Имена котиков' in user_text_clean:
            await update.message.reply_text("Барсик и Пушок", reply_markup=self.main_keyboard)
            return True
        elif "Назад" in user_text_clean:
            await update.message.reply_text("Возвращаемся в главное меню", reply_markup=self.main_keyboard)
            return True
        elif user_text_clean == 'Инфа':
            await self.info(update, context)
            return True
        elif user_text_clean == 'Сколько сейчас времени?' or user_text_clean == "Сколько времени?":
            await self.day_time(update, context)
            return True
        elif user_text_clean == 'Автор':
            await self.author(update, context)
            return True
        elif user_text_clean == 'Задать вопрос':
            await update.message.reply_text(
                "Выберите вопрос из меню:",
                reply_markup=self.questions_keyboard
            )
            return True

        elif user_text_clean == 'Доступные команды':
            await self.available_commands(update, context)
            return True
        elif user_text_clean == 'Сколько времени?':
            await self.day_time(update, context)

        print(f"DEBUG: Текст не распознан: '{user_text_clean}'")
        return False