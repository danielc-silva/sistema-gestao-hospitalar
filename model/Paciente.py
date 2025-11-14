from .Pessoa import Pessoa
from datetime import date, time, datetime, timedelta
from .Prontuario import Prontuario

class Paciente (Pessoa):
    def __init__(self, nome=None, cpf=None, data_nascimento=None, id_hosp = None):
        super().__init__(nome, cpf, data_nascimento)
        self.id_hosp = id_hosp
        self.__prontuario = Prontuario(self)

    @property
    def id_hosp (self):
        return self.__id_hosp
    
    @id_hosp.setter
    def id_hosp (self, id_recebido):
        if (id_recebido  == None):
            raise ValueError ("O campo ID Hospitalar é obrigatório.")
        self.__id_hosp = id_recebido.upper()

    @property
    def prontuario (self):
        return self.__prontuario
    
    def papel_da_pessoa(self):
        return "Paciente"
    
    def __str__(self):
        infos = "\n=== INFORMAÇÕES DO PACIENTE ==="
        infos += super().__str__()
        infos += (f"\nID Hospitalar: {self.id_hosp}")

        return infos
