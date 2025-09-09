import logging
import asyncio

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename="hobby.log",
    filemode='a',
    encoding='utf-8',
    format="%(asctime)s -%(levelname)s -%(message)s"
)

async def cats(cat: str):
    await asyncio.sleep(1)
    logging.info("%s mya yyy....", cat)

asyn
