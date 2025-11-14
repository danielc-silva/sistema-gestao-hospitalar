from datetime import date, time, datetime, timedelta
from .Medico import Medico
from .StatusFuncionario import StatusFuncionario

class Prontuario:
    def __init__(self, paciente_dono):
        self.__paciente_dono = paciente_dono
        self.__entradas = []

    def atualizar_entradas (self, medico : Medico, descricao):
        if (medico.status !=StatusFuncionario.ATIVO):
            print(f"\nATENÇÃO: Não foi possivel atualizar o prontuario do paciente pois o Dr. {medico.nome} se encontra {medico.status.value} no momento.")
            return
        hoje = datetime.now()
        infos = f"\nEntrada: {hoje.strftime('%d/%m/%Y às %H:%M')}"
        infos += f"\nMédico: {medico.nome}"
        infos += f"\nDescrição: {descricao}"
        self.__entradas.append(infos)
        return
    
    def mostrar_prontuario (self):
        pront = (f'\n=======> PRONTUARIO DE {self.__paciente_dono.nome.upper()} <=======\n')
        tamanhao_para_formatacao = (len(pront)) - 2
        pront += '=' * tamanhao_para_formatacao
        for infos in (self.__entradas):
            pront += (f'{infos}\n')
            pront += '=' * tamanhao_para_formatacao
        pront += ('\n')
        return pront