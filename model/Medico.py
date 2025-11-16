from .Funcionario import Funcionario
from .StatusFuncionario import StatusFuncionario

class Medico (Funcionario):
    def __init__(self, nome=None,
                 cpf=None,
                 data_nascimento=None,
                 id_funcionario=None,
                 salario=None, status=None,
                 crm = None,
                 especialidade = None):
        super().__init__(nome, cpf, data_nascimento, id_funcionario, salario, status)
        self.crm = crm
        self.especialidade = especialidade

    @property
    def crm (self):
        return self.__crm
    
    @crm.setter
    def crm (self, crm_recebido):
        if (crm_recebido == None):
            raise ValueError ("Campo CRM é obrigatório.")
        self.__crm = crm_recebido.upper()

    @property
    def especialidade (self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade (self, especialidade_recebida):
        if (especialidade_recebida == None):
            raise ValueError ("O campo Especialidade é obrigatório.")
        self.__especialidade = especialidade_recebida

    def __str__(self):
        infos = "\n=== INFORMAÇÕES DO MÉDICO ==="
        infos += super().__str__()
        infos += (f"\nCRM: {self.crm}")
        infos += (f"\nEspecialidade: {self.especialidade}")
        return infos
    
    def trabalhar(self):
         if (self.status !=StatusFuncionario.ATIVO):
            return (f"\nATENÇÃO: Não foi é possível solicitar que o Dr. {self.nome} trabalhe pois ele se encontra {self.status.value} no momento.")
         return (f"Dr. {self.nome} está atendendo pacientes.")
    
    def papel_da_pessoa(self):
        return "Medico"