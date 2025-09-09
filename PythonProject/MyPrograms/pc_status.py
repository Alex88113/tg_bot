import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename="pc_status.log",
    filemode="w",
    format="%(asctime)s -%(levelname)s -%(message)s",
    encoding='utf-8'
)

class PcStatus(ABC):
    def __init__(self, status_pc=False, internet_network=True, electricity=True):
        self._status_pc = status_pc
        self._internet_network = internet_network
        self._electricity = electricity

    def log_status_pc(self):
        logging.info("Статус вашего пк: %s", self._status_pc)
        logging.info("Состояние интернет - сети: %s", self._internet_network)
        logging.info("Наличие электропитания: %s", self._electricity)

    @abstractmethod
    def check_status_pc(self):
        pass

class ChekPcStatus(PcStatus):
    def check_status_pc(self):
        try:
            user = input("Хоти те ли вы увидеть статус своего пк, электроэнергии и доступа в интернет сеть?: ").strip().lower()
            if user == 'yes':
                list_status = {
                    "status_pc": self._status_pc,
                    "internet network": self._internet_network,
                    "electricity": self._electricity
                }
                print("Вся информация находится в логе с ником 'pc_status.log")
                logging.info(list_status)
        except Exception as e:
            logging.error(e)
            return None

def main():
    result = ChekPcStatus(status_pc=False, internet_network=True, electricity=True)
    result.check_status_pc()

if __name__ == "__main__":
    main()
ё