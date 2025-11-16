from .Medico import Medico
from .Enfermeiro import Enfermeiro

class FuncionarioFactory():
    @staticmethod
    def criar_funcionario(tipo_do_funcionario : str, **args):
        if tipo_do_funcionario == 'Medico':
            return Medico(nome= args.get('nome', None),
                             cpf= args.get('cpf', None),
                             data_nascimento= args.get('data_nascimento', None),
                             id_funcionario= args.get('id_funcionario', None),
                             salario= args.get('salario', None),
                             status= args.get('status', None),   
                             crm= args.get('crm', None), 
                             especialidade= args.get('especialidade', None), 
                             )
        elif tipo_do_funcionario == 'Enfermeiro':
            return Enfermeiro(nome= args.get('nome', None),
                             cpf= args.get('cpf', None),
                             data_nascimento= args.get('data_nascimento', None),
                             id_funcionario= args.get('id_funcionario', None),
                             salario= args.get('salario', None),
                             status= args.get('status', None),   
                             coren= args.get('coren', None), 
                             )
        else:
            raise ValueError(f'Tipo de funcionário desconhecido: {tipo_do_funcionario}')
