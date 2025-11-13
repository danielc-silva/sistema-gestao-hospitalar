from datetime import date, time, datetime, timedelta
from .Paciente import Paciente

class Prontuario ():
    def __init__ (self, paciente : Paciente):
        self.__entrada = []

# conferir essa ideia de prontuario 