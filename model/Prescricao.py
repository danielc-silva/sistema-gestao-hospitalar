from .Medico import Medico
from .Paciente import Paciente
from .Exame import Exame

class Prescricao ():
    def __init__(self, medico_solicitante : Medico = None, paciente  : Paciente = None):
        self.medico_solicitante = medico_solicitante
        self.paciente = paciente
        self.__lista_exames = []
        self.__lista_medicamentos = []

    @property
    def medico_solicitante (self):
        return self.__medico_solicitante   
    
    @medico_solicitante.setter
    def medico_solicitante (self, medico_recebido):
        if (medico_recebido == None):
            raise ValueError ("O campo Médico Solicitante é obrigatório.")
        if not isinstance(medico_recebido, Medico):
            raise TypeError("O médico solicitante deve ser uma instância da classe Medico.")
        self.__medico_solicitante = medico_recebido

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

    def __str__(self):
        infos = f"\nMédico: {self.medico_solicitante.nome}"
        infos += f"\nPaciente: {self.paciente.nome}"
        return infos
    
    def adicionar_exame (self, exame : Exame):
        if not isinstance(exame, Exame):
            raise TypeError("O exame deve ser uma instância da classe Exame.")
        self.__lista_exames.append(exame)

    def adicionar_medicamento (self, medicamento : str):
        if not isinstance(medicamento, str):
            raise TypeError("O medicamento deve ser uma string.")
        self.__lista_medicamentos.append(medicamento)

    def lista_exames_solicitados (self):
        infos = "\n======= Exames Solicitados ======="
        for exame in self.__lista_exames:
            infos += f"{exame}"
        infos += "\n==================================="
        return infos
    
    def listar_medicamentos_prescritos (self):
        infos = "\n===== Medicamentos Prescritos ====="
        for medicamento in self.__lista_medicamentos:
            infos += f"\n {medicamento}"
        infos += "\n==================================="  
        return infos
    
    def __str__(self):
        infos = "\n======== PRESCRIÇÃO MÉDICA ========"
        infos += f"\nMédico: {self.medico_solicitante.nome}"
        infos += f"\nPaciente: {self.paciente.nome}"
        infos += "\n==================================="
        infos += self.lista_exames_solicitados()
        infos += self.listar_medicamentos_prescritos()
        return infos
    
    def realizar_exames (self):
        infos = "\n========= Realizando dos Exames ========="
        for exame in self.__lista_exames:
            infos += exame.realizar_exame(self.paciente)
        infos += "\n====================================="
        return infos



