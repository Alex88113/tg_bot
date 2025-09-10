# Используем официальный легкий образ Python
FROM python:3.11-slim-bullseye

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Сначала копируем файл с зависимостями (используется кэш Docker)
COPY ./app/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта в рабочую директорию
COPY ./app .

# Запускаем бота когда контейнер запустится
CMD ["python", "bot.py"]
