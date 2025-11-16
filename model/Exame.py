from abc import ABC, abstractmethod
from .Paciente import Paciente

class Exame (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def realizar_exame(self, paciente_alvo : Paciente):
        pass

    @abstractmethod
    def __str__(self):
        pass