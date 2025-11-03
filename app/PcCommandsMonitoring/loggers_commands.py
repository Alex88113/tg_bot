from loguru import logger
import asyncio
import functools

error_logger = logger.bind(log_type='ERROR')
error_logger.add(
    'logs/error.log',
    level='ERROR',
    filter=lambda record: record['extra'].get("log_type") == 'ERROR',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}\n{exception}",
    encoding='utf-8'
)
debug_logger = logger.bind(log_type='DEBUG')
debug_logger.add(
    "logs/debug.log",
    level='DEBUG',
    filter= lambda record: record['extra'].get('log_type') == 'DEBUG',
    format="{time:YYYY-MM-DD HH:mm:ss} | DEBUG | {module}:{function}:{line} | {message}",
    encoding='utf-8'
)
result_logger = logger.bind(log_type='RESULT')
result_logger.add(
    'logs/result_work.log',
    level='INFO',
    filter=lambda record: record['extra'].get("log_type") == 'RESULT',
    format='{time:YYYY-MM-DD HH:mm:ss} | RESULT | {message}',
    encoding='utf-8'
)

def loger_decorator(func):
    functools.wraps(func)
    async def wrapper(*args, **kwargs):
        debug_logger.debug(f'Запущен метод {func.__name__}')
        result = await func(*args, **kwargs)
        result_logger.info(f'Результат работы метода {func.__name__}: {result}')
        debug_logger.debug(f'Работа метода {func.__name__} завершена\n')
        return result
    return wrapper

