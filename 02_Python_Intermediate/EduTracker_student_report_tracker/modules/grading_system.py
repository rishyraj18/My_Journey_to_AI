from abc import ABC , abstractmethod

class GradingSystem(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass