from .Consulta import Consulta
from .Medico import Medico  
from .Paciente import Paciente
from .EstrategiasPagamento import EstrategiaPagamento, PagamentoParticular
from datetime import datetime

class SistemaAgendamento ():
    def __init__(self):
        self.consultas = []

    def agendar_consulta(self, medico : Medico,
                        paciente : Paciente,
                        data_hora : datetime,
                        estrategia_pagamento: EstrategiaPagamento = None):
        
        nova_consulta = Consulta(
            medico=medico,
            paciente=paciente,
            data_hora=data_hora,
            status_consulta="Agendada",
            estrategia_pagamento=estrategia_pagamento
        )

        self.consultas.append(nova_consulta)
        return nova_consulta
    
    def __str__(self):
        if not self.consultas:
            return "\nNenhuma consulta agendada no momento."
        
        infos = "\n========= CONSULTAS AGENDADAS ========="
        for i in self.consultas :
            infos += f"\n{(i).__str__()}" # vou utilizar diretamente pois vou jogar o retorno em uma string unica
        infos += "\n======================================="
        return infos