import asyncio
from telegram import Update
from telegram.ext import ContextTypes
import platform
import psutil
from abc import ABC, abstractmethod
from datetime import datetime

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
    @abstractmethod
    async def users_system(self, update, context):
        pass
    @abstractmethod
    async def access_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def time_start_system(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

class PcCommandsBot(PcCommands):
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
    partitions = psutil.disk_partitions(all=False)
    info_disk = '💾 Информация о дисках:\n\n'
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            info_disk += f"""📁 Раздел диска: {partition.mountpoint}
   Тип файловой системы: {partition.fstype}
   💽 Всего: {usage.total // (1024 ** 3)} GB
   🔴 Использовано: {usage.used // (1024 ** 3)} GB ({usage.percent}%)
   🟢 Свободно: {usage.free // (1024 ** 3)} GB\n\n"""

        except Exception as error:
            info_disk += f"❌ Ошибка: {error}\n\n"
    await update.message.reply_text(info_disk)

    async def users_system(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        users = psutil.users()
        for user in users:
            await update.message.reply_text(f"Текущий пользователь системы: {user}")

    async def access_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        virtual_memory = psutil.virtual_memory()
        all_info_memory = f"""
        Всего ОЗУ: {virtual_memory.total / (1024 ** 3):.2f} gb
Доступно: {virtual_memory.available / (1024 ** 3):.2f} gb
Использовано: {virtual_memory.used / (1024 ** 3):.2f} gb
Процент использования: {virtual_memory.percent}%
Свободно: {virtual_memory.free / (1024 ** 3):.2f} gb"""
        await update.message.reply_text(all_info_memory)

    async def time_start_system(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        boot_time = psutil.boot_time()
        await update.message.reply_text(f"Время загрузки системы: {datetime.fromtimestamp(boot_time)}")
        uptime = datetime.now() - datetime.fromtimestamp(boot_time)
        await update.message.reply_text(f"Аптайм: {uptime}")
