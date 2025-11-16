from .Prescricao import Prescricao
from .Medico import Medico
from .Paciente import Paciente
from datetime import datetime 

class Consulta ():
    def __init__(self, medico : Medico = None, paciente : Paciente = None, data_hora : datetime = None):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora
        self.prescricao = None

    @property
    def medico (self):
        return self.__medico   
    
    @medico.setter
    def medico (self, medico_recebido):
        if (medico_recebido == None):
            raise ValueError ("O campo Médico é obrigatório.")
        if not isinstance(medico_recebido, Medico):
            raise TypeError("O médico deve ser uma instância da classe Medico.")
        self.__medico = medico_recebido

    @property
    def paciente (self):
        return self.__paciente  

    @paciente.setter
    def paciente (self, paciente_recebido): 
        if (paciente_recebido == None):
            raise ValueError ("O campo Paciente é obrigatório.")
        if not isinstance(paciente_recebido, Paciente):
            raise TypeError("O paciente deve ser uma instância da classe Paciente.")
        self.__paciente = paciente_recebido

    @property
    def data_hora (self):
        return self.__data_hora  

    @data_hora.setter
    def data_hora (self, data_recebida, hora_recebida): 
        if ((data_recebida == None) or (hora_recebida == None)):
            raise ValueError ("Os campos Data e Hora são obrigatórios.")
        data_hora_recebida = f"{data_recebida} {hora_recebida}"
        try:
             data_hora_recebida = datetime.strptime(data_hora_recebida, "%d-%m-%Y %H:%M")
        except ValueError:
             raise ValueError(f"Formato inválido. Use DD-MM-AAAA e HH:MM. Recebido: {data_hora_recebida}")
        self.__data_hora = data_hora_recebida

    def adicionar_prescricao (self, prescricao : Prescricao):
        if not isinstance(prescricao, Prescricao):
            raise TypeError("A prescrição deve ser uma instância da classe Prescricao.")
        self.prescricao = prescricao