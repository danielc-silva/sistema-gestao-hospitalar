from .Funcionario import Funcionario
from .StatusFuncionario import StatusFuncionario

class Enfermeiro (Funcionario):
    def __init__(self, nome=None, cpf=None, data_nascimento=None, id_funcionario=None, salario=None, status=None, coren = None):
        super().__init__(nome, cpf, data_nascimento, id_funcionario, salario, status)
        self.coren = coren

    @property
    def coren (self):
        return self.__coren
    
    @coren.setter
    def coren (self, coren_recebido):
        if (coren_recebido == None):
            raise ValueError ("O campo COREN é obrigatório.")
        self.__coren = coren_recebido.upper()

    def papel_da_pessoa(self):
        return 'Enfermeiro'
    
    def __str__(self):
        infos = "\n=== INFORMAÇÕES DO ENFERMEIRO ==="
        infos += super().__str__()
        infos += (f"\nCOREN: {self.coren}")
        return infos
    
    def trabalhar(self):
         if (self.status !=StatusFuncionario.ATIVO):
            return (f"\nATENÇÃO: Não foi é possível solicitar que o Enfermeiro {self.nome} trabalhe pois ele se encontra {self.status.value} no momento.")
         return (f"\nO enfermeiro {self.nome} está aplicando medicamentos nos pacientes paliativos.")