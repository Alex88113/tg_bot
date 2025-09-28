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

    #@abstractmethod
    #async def hide_keyboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        #pass

class CommandsMyBot(CommandsBot):
    def __init__(self) -> None:
        self.main_keyboard = ReplyKeyboardMarkup(
            [
                ['Команды', 'Информация'],
                ['Время', 'Автор'],
                ['Задать вопрос', 'Имена котиков'],
                ['Cписок дел', 'Скрыть кнопки']
            ],
            resize_keyboard=True,
            input_field_placeholder="Выберите действие"
        )

        self.questions_keyboard = ReplyKeyboardMarkup(
            [
                ['Сколько времени?', 'Список дел'],
                ['Имена моих котиков', 'Назад']
            ],
            resize_keyboard=True
        )

        self.todo_list = ["sport", "programming", "college", "codding 40 min"]

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_text = (
            "Я твой персональный ассистент для управления твоим ПК!\n\n"
            "Юзай кнопки ниже для взаимодействия со мной:"
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
2. Информация - о боте
3. Время - текущее время дата, день недели и год
4. Автор - об авторе
5. Задать вопрос - меню вопросов
6. Имена котиков - показать имена котиков
7. Cписок дел - показать список дел
8. Скрыть кнопки - убрать клавиатуру"""

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
        user_text_clean = user_text.lower().strip()

        if 'как зовут моих двух котиков?' in user_text_clean or 'имена котиков' in user_text_clean:
            await update.message.reply_text("Барсик и Пушок")
            return True

        elif "выведи мой список дел на сегодня" in user_text_clean or "список дел" in user_text_clean:
            list_dela = ['На сегодня планов нет']
            await update.message.reply_text(list_dela)
            return True

        elif "сколько сейчас времени?" in user_text_clean or "сколько времени?" in user_text_clean:
            time_now = datetime.now().strftime("%H:%M:%S")
            await update.message.reply_text(f"Сейчас: {time_now} часов", reply_markup=self.main_keyboard)
            return True

        elif "назад" in user_text_clean:
            await update.message.reply_text("Возвращаемся в главное меню", reply_markup=self.main_keyboard)
            return True
        else:
            return "Ой...я не знаю ответа на этот вопрос.\nНапечатайте команду /avalilable_commands"