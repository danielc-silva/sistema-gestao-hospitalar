from .Medico import Medico
from .Enfermeiro import Enfermeiro
from .Paciente import Paciente


class PessoaFactory():
    @staticmethod
    def criar_pessoa(tipo_da_pessoa : str, **args):
        if tipo_da_pessoa == 'Medico':
            return Medico(nome= args.get('nome', None),
                             cpf= args.get('cpf', None),
                             data_nascimento= args.get('data_nascimento', None),
                             id_funcionario= args.get('id_funcionario', None),
                             salario= args.get('salario', None),
                             status= args.get('status', None),   
                             crm= args.get('crm', None), 
                             especialidade= args.get('especialidade', None), 
                             )
        elif tipo_da_pessoa == 'Enfermeiro':
            return Enfermeiro(nome= args.get('nome', None),
                             cpf= args.get('cpf', None),
                             data_nascimento= args.get('data_nascimento', None),
                             id_funcionario= args.get('id_funcionario', None),
                             salario= args.get('salario', None),
                             status= args.get('status', None),   
                             coren= args.get('coren', None), 
                             )
        elif tipo_da_pessoa == 'Paciente':
            return Paciente(nome= args.get('nome', None),
                             cpf= args.get('cpf', None),
                             data_nascimento= args.get('data_nascimento', None),
                             id_hosp = args.get('id_paciente', None),
                             )  
        else:
            raise ValueError(f'Tipo de pessoa desconhecido: {tipo_da_pessoa}')
    