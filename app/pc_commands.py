import asyncio
from telegram import Update
from telegram.ext import ContextTypes
import platform
import psutil

from abc import ABC, abstractmethod
from datetime import datetime

class PcCommands(ABC):
    @abstractmethod
    async def test(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def system_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def processor_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def disk(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def access_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

class PcCommandsBot(PcCommands):
    async def test(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Простая тестовая команда"""
        print("✅ Команда /test вызвана")
        await update.message.reply_text("✅ Бот работает! Команда /test выполнена.")

    async def system_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        system = platform.system()
        architecture = platform.architecture()
        await update.message.reply_text(f"Ваша ОС: {system}\nАрхитектура вашего пк: {architecture}")

    async def processor_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
         model_processor = platform.processor()
         machine_processor = platform.machine()
         await update.message.reply_text('-' * 80)
         await update.message.reply_text(f"Модель процессора вашего пк: {model_processor}\nАрхитектура вашего процессора: {machine_processor}")
         await update.message.reply_text(f'Кол во ядер: {psutil.cpu_count()}')
         await update.message.reply_text(f'Кол во физических ядер: {psutil.cpu_count(logical=False)}')
         cpu_freq = psutil.cpu_freq()
         await update.message.reply_text(f"Текущая частота: {cpu_freq.current} MHz")
         await update.message.reply_text(f'Минимальная частота: {cpu_freq.min}')
         await update.message.reply_text(f'Максимальная частота: {cpu_freq.max}')
         await update.message.reply_text('-' * 80)

    async def disk(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        info_about_disk = psutil.disk_partitions()
        for data_disk in info_about_disk:
            used = psutil.disk_usage('/')
            all_data_disk = f"""
Диск: {data_disk.device}
Точка монтирования: {data_disk.mountpoint}
Файловая система: {data_disk.fstype}
Общий объём диска {data_disk.device}: {used.total / (1024 ** 3):.2f}"""
            await update.message.reply_text(all_data_disk)
    
    async def access_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        virtual_memory = psutil.virtual_memory()
        used_memory = (virtual_memory.used / virtual_memory.total) * 100
        all_data_memory = f"""
Общий объём ОЗУ: {virtual_memory.total / (1024 ** 3):.2f}GB
Свободно: {virtual_memory.available / (1024 ** 3):.2f}GB
Используется: {used_memory:.2f}%"""
        await update.message.reply_text(all_data_memory)
