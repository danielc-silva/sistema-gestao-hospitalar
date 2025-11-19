from .Consulta import Consulta
from .Medico import Medico  
from .Paciente import Paciente
from .EstrategiasPagamento import EstrategiaPagamento, PagamentoParticular
from datetime import datetime

class SistemaAgendamento ():
    def __init__(self):
        self.consultas = []

    def agendar_consulta(self, codigo_consulta: int,
                        medico : Medico,
                        paciente : Paciente,
                        data_hora : datetime,
                        estrategia_pagamento: EstrategiaPagamento = None):
        
        nova_consulta = Consulta(
            codigo_consulta = codigo_consulta,
            medico=medico,
            paciente=paciente,
            data_hora=data_hora,
            status_consulta="Agendada",
            estrategia_pagamento=estrategia_pagamento
        )

        self.consultas.append(nova_consulta)
        return nova_consulta
    

    def adicionar_prescricao_consulta(self, cod_consult, prontuario : str):
        for consulta in self.consultas:
            if consulta.codigo_consulta == cod_consult:
                consulta.adicionar_prescricao(prontuario)
                return consulta.paciente.prontuario
        raise ValueError(f"Consulta com código {cod_consult} não encontrada.")

    
    def __str__(self):
        if not self.consultas:
            return "\nNenhuma consulta agendada no momento."
        
        infos = "\n========= AGENDA DE CONSULTAS ========="
        for i in self.consultas :
            infos += f"\n{(i).__str__()}" # vou utilizar diretamente pois vou jogar o retorno em uma string unica
        return infos