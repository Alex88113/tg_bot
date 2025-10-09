import asyncio
from telegram import Update
from telegram.ext import ContextTypes
import platform
import psutil
from abc import ABC, abstractmethod

class PcCommands(ABC):
    @abstractmethod
    async def system_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def processor_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def disk(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
class PcCommandsBot(PcCommands):
    async def system_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        system = platform.system()
        architecture = platform.architecture()
        await update.message.reply_text(f"Ваша ОС: {system}\nАрхитектура вашего пк: {architecture}")

    async def processor_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
         model_processor = platform.processor()
         machine_processor = platform.machine()
         await update.message.reply_text(f"Модель процессора вашего пк: {model_processor}\nАрхитектура вашего процессора: {machine_processor}")

    async def disk(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        partitions = psutil.disk_partitions(all=False)
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                await update.message.reply_text(f"\nФайловая система: {partition.fstype}\nОпции: {partition.opts}\nВсего: {usage.total // (1024**3)} GB\nИспользовано: {usage.used // (1024 ** 3)} gb ({usage.percent}%\nСвободно: {usage.free // (1024 ** 3)}  gb")
            except Exception as error:
                return f"error in: {error}"