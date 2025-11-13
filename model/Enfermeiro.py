from .Funcionario import Funcionario

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
        infos = "INFORMAÇÕES DO ENFERMEIRO"
        infos += super().__str__()
        infos += (f"\nCOREN: {self.coren}")
        return infos
    
    def trabalhar(self):
        return (f"\nO enfermeiro {self.nome} está aplicando medicamentos nos pacientes paliativos.")