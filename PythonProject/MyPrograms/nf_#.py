import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename="result_work_class.log",
    filemode="a",
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
)

            
class Animals(ABC):
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound
        
    def log_animals(self):
        logging.info("Животинка по имени: %s", self.name)
        logging.info("Издаёт звук: %s", self.sound)
        logging.info("============================")
          
    @abstractmethod
    def name_animals(self) -> str:
        pass
    
    @abstractmethod
    def sound_animals(self) -> str:
        pass

class Dog(Animals):
    def name_animals(self) -> str:
        return f"У нас в зоопарке новый друг его имя: {self.name}"
    
    def sound_animals(self) -> str:
        return f"{self.name} произносит звук: {self.sound}"

class Cat(Animals):
    def name_animals(self) -> str:
        return f"Держите своего котика, его зовут: {self.name}"
    
    def sound_animals(self) -> str:
        return f"{self.name} испускает звук {self.sound}"
    
def test_methods():
    list_animals = [
        Dog("Mike", "gav...gav"),
        Cat("Barsik", "Myauuuuuu")
        ]
    
    for animals in list_animals:
        print(animals.name_animals())
        print(animals.sound_animals())
        animals.log_animals()
        print()
        
if __name__ == "__main__":
    test_methods()
