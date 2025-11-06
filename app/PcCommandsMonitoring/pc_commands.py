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
    async def access_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass
    @abstractmethod
    async def collecting_network_statistics(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
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
         processor = psutil.cpu_times()
         await update.message.reply_text('-' * 80)
         await update.message.reply_text(f"Ваш компьютер простаивал в обычном пользовательском режиме: {processor.user:.2f} секунд")
         await update.message.reply_text(f"Время выполнения кода ядра процессора ос: {processor.system:.2f} секунд")
         await update.message.reply_text(f"Процессор простаивал: {processor.idle} секунд")


    async def disk(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            usage = psutil.disk_usage('/')
            data_disk = ""
            data_disk += f"Размер всего диска: {usage.total / (1024 ** 3):.2f}GB\n"
            data_disk += f"Используется: {(usage.used / usage.total) * 100:.2f}%\n"
            data_disk += f"Свободного места: {(usage.free / usage.total) * 100:.2f}\n"
            await update.message.reply_text(data_disk)
        except OSError as error:
            await update.message.reply_text(f'возникла ошибка с путем к диску: {error}')


    async def access_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        virtual_memory = psutil.virtual_memory()
        used_memory = (virtual_memory.used / virtual_memory.total) * 100
        all_data_memory += "=================Данные о оперативной памяти вашего пк================="
        all_data_memory += f"Общий объём ОЗУ: {virtual_memory.total / (1024 ** 3):.2f}GB"
        all_data_memory += f"Общий объём ОЗУ: {virtual_memory.total / (1024 ** 3):.2f}GB"
        all_data_memory += f"Свободно: {virtual_memory.available / (1024 ** 3):.2f}GB"
        all_data_memory += f"Используется: {used_memory:.2f}%"
        all_data_memory +=  '========================================================================'
        await update.message.reply_text(all_data_memory)


    async def collecting_network_statistics(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        net_io = psutil.net_io_counters()
        per_nic_io = psutil.net_io_counters(pernic=True)

        data_about_network = "Сетевая статистика\n"
        data_about_network += "=" * 50 + "\n"
        data_about_network += f"Общее отправлено: {net_io.bytes_sent / (1024 ** 3):.2f} GB\n"
        data_about_network += f"Общее получено: {net_io.bytes_recv / (1024 ** 3):.2f} GB\n"
        data_about_network += f"Общее кол-во пакетов: {net_io.packets_recv}\n\n"

        data_about_network += "Статистика по сетевым интерфейсам:\n"
        data_about_network += "-" * 50 + "\n"

        for nic_name, stats in per_nic_io.items():
            await asyncio.sleep(0.1)
            data_about_network += f"Интерфейс: {nic_name}\n"
            data_about_network += f"  Отправлено: {stats.bytes_sent / (1024 ** 2):.2f} MB\n"
            data_about_network += f"  Получено: {stats.bytes_recv / (1024 ** 2):.2f} MB\n"
            data_about_network += f"  Пакеты отправлено: {stats.packets_sent}\n"
            data_about_network += f"  Пакеты получено: {stats.packets_recv}\n"
            data_about_network += f"  Ошибки: {stats.errin} входящих, {stats.errout} исходящих\n"
            data_about_network += "-" * 30 + "\n"

        await update.message.reply_text(data_about_network)
