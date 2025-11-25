from .Pessoa import Pessoa
from datetime import date, time, datetime, timedelta
from abc import ABC, abstractmethod
from .StatusFuncionario import StatusFuncionario

class Funcionario (Pessoa, ABC):
    def __init__(self, nome=None, cpf=None, data_nascimento=None, id_funcionario = None, salario = None, status = None):
        super().__init__(nome, cpf, data_nascimento)
        self.id_funcionario = id_funcionario 
        self.salario = salario
        self.__historico_funcionario = [] # no setter do status já atualiza o histórico
        self.status = status

    @property
    def id_funcionario (self):
        return self.__id_funcionario
    
    @id_funcionario.setter
    def id_funcionario (self, id_recebido):
        if (id_recebido == None):
            raise ValueError ("O campo ID é obrigatório.")
        self.__id_funcionario = id_recebido.upper()

    @property
    def salario (self):
        return self.__salario
    
    @salario.setter
    def salario (self, valor):
        if (valor == None):
            raise ValueError ("O campo Salário é obrigatório.")
        if not isinstance(valor, (int, float)):
            raise TypeError("O salário deve ser um número.")
        if (valor < 0.00):
            raise ValueError ("O sálario não pode ser negativo.")
        self.__salario = valor

    @property
    def status (self):
        return self.__status
    
    @status.setter
    def status (self, status_recebido):
        if status_recebido is None:
            novo_status = StatusFuncionario.ATIVO
        elif isinstance(status_recebido, StatusFuncionario):
            novo_status = status_recebido
        elif isinstance(status_recebido, str):
             try:
                 novo_status = StatusFuncionario[status_recebido.upper()]
             except KeyError:
                 try:
                    novo_status = StatusFuncionario(status_recebido)
                 except ValueError:
                    raise ValueError(f"Status: '{status_recebido}' é inválido. Use um membro de StatusFuncionario.")
        else:
            raise TypeError("O status deve ser do tipo StatusFuncionario ou string.")
            # lembrando aqui só entra c o usuario tentar mandar um int ou float
        self.__status = novo_status
        self.atualizar_historico()
    
    def __str__(self):
        infos = super().__str__()
        infos += (f"\nID: {self.id_funcionario}")
        infos += (f"\nSalário: R${self.salario:.2f}")
        infos += (f"\nStatus: {self.status.value}")
        return infos
    
    def mostrar_historico (self):
        hist = (f'\nHistórico do funcionario [{self.nome}: {self.papel_da_pessoa()}]\n')
        tamanho_para_formatacao = len(hist)
        hist += "=" * tamanho_para_formatacao
        for historico in (self.__historico_funcionario):
            hist += (f'\n{historico}')
        hist += "\n"
        hist += "=" * tamanho_para_formatacao
        hist += ('\n')
        return hist
    
    def afastar_funcionario (self):
        self.status = StatusFuncionario.AFASTADO
        return

    def ferias_funcionario (self):
        self.status = StatusFuncionario.FERIAS
        return

    def ativar_funcionario (self):
        self.status = StatusFuncionario.ATIVO
        return
    
    def aviso_previo_funcionario (self):
        self.status = StatusFuncionario.AVISO_PREVIO
        return

    def desligar_funcionario (self):
        self.status = StatusFuncionario.DESLIGADO
        

    def atualizar_historico (self):
        hoje = datetime.now()
        info = (f'Status alterado para ({self.status.value}) em {hoje.strftime("%d-%m-%Y")}')
        self.__historico_funcionario.append(info)
        return

    @abstractmethod
    def trabalhar (self):
        pass

    @abstractmethod
    def papel_da_pessoa(self):
        pass