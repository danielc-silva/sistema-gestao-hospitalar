from datetime import date, time, datetime, timedelta
from abc import ABC, abstractmethod

class Pessoa (ABC):
    def __init__(self, nome = None, cpf = None, data_nascimento = None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    @property
    def nome (self):
        return self.__nome 
    
    @nome.setter
    def nome (self, nomee):
        if (nomee == None):
            raise ValueError (f"Nome é um campo obrigatório.")
        self.__nome = nomee.title()

    @property
    def cpf (self):
        return self.__cpf
    
    @cpf.setter
    def cpf (self, CPF):
        if CPF is None:
             raise ValueError("O CPF é um campo obrigatório.")
        tam = len(CPF)
        if not ((tam == 11) and (CPF.isdigit())):
            raise ValueError(f"O CPF '{CPF}' é inválido. Deve conter 11 dígitos numéricos.")
            
        self.__cpf = CPF
       
    @property
    def data_nascimento (self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento (self, data_recebida):
        if data_recebida is None:
            raise ValueError ("A Data de Nascimento é um campo obrigatório.")
        hoje = datetime.now()
        try:
            data_convertida = datetime.strptime(data_recebida, "%d-%m-%Y") 
        except ValueError:
            raise ValueError(f"Formato de data '{data_recebida}' inválido. Por favor, use o formato DD-MM-AAAA.") 
        if ((data_convertida > hoje)):
            raise ValueError ("A Data de Nascimento deve ser válida.")
        self.__data_nascimento = data_convertida.date()

    def __str__(self):
        infos = ''
        infos += (f"\nNome: {self.nome}")
        infos += (f"\nCPF: {self.cpf}")
        infos += (f"\nData de Nascimento: {self.data_nascimento}")  
        return infos 
    
    @abstractmethod
    def papel_da_pessoa (self):
        pass

    # A ideia é que cada filha diga o papel é (Funcionario, Paciente, ...)