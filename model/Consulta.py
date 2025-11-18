from .Prescricao import Prescricao
from .Medico import Medico
from .Paciente import Paciente
from datetime import datetime 
from .StatusConsulta import StatusConsulta
from .StatusFuncionario import StatusFuncionario
from .EstrategiasPagamento import EstrategiaPagamento, PagamentoParticular

class Consulta ():

    VALOR_BASE = 400.00 # defini esse valor pra aplicar o strategy pattern depois

    def __init__(self, medico : Medico = None,
                paciente : Paciente = None,
                data_hora : datetime = None,
                status_consulta = None,
                estrategia_pagamento: EstrategiaPagamento = None):
                
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora
        self.prescricao = None
        self.status_consulta = status_consulta
        self.estrategia_pagamento = estrategia_pagamento

    @property
    def estrategia_pagamento(self):
        return self.__estrategia_pagamento

    @estrategia_pagamento.setter
    def estrategia_pagamento(self, estrategia_recebida):
        # Se não passar nada, assumimos o padrão "Particular"
        if estrategia_recebida is None:
            self.__estrategia_pagamento = PagamentoParticular()
        
        # Se passar, tem que ser uma filha de EstrategiaPagamento
        elif isinstance(estrategia_recebida, EstrategiaPagamento):
            self.__estrategia_pagamento = estrategia_recebida
        
        else:
            raise TypeError("A estratégia deve herdar de EstrategiaPagamento.")

    @property
    def medico (self):
        return self.__medico   
    
    @medico.setter
    def medico (self, medico_recebido):
        if (medico_recebido.esta_disponivel_para_consulta() != True):
            raise ValueError (f"ERRO: Atenção, o médico deve estar [Ativo] para agendar uma consulta.")
        if (medico_recebido == None):
            raise ValueError ("O campo Médico é obrigatório.")
        if not isinstance(medico_recebido, Medico):
            raise TypeError("O médico deve ser uma instância da classe Medico.")
        self.__medico = medico_recebido

    @property
    def paciente (self):
        return self.__paciente  

    @paciente.setter
    def paciente (self, paciente_recebido): 
        if (paciente_recebido == None):
            raise ValueError ("O campo Paciente é obrigatório.")
        if not isinstance(paciente_recebido, Paciente):
            raise TypeError("O paciente deve ser uma instância da classe Paciente.")
        self.__paciente = paciente_recebido

    @property
    def data_hora (self):
        return self.__data_hora  

    @data_hora.setter
    def data_hora(self, data_hora_recebida):
        if data_hora_recebida is None:
            raise ValueError("Os campos Data e Hora são obrigatórios.")
        # aqui no caso que já venha um datetime certinho
        if isinstance(data_hora_recebida, datetime):
            self.__data_hora = data_hora_recebida
        # se o usuario mandou apenas um texto tenta converter
        elif isinstance(data_hora_recebida, str):
            try:
                self.__data_hora = datetime.strptime(data_hora_recebida, "%d-%m-%Y %H:%M")
            except ValueError:
                raise ValueError(f"Formato inválido. Use DD-MM-AAAA HH:MM. Recebido: {data_hora_recebida}")
        else: # mandaram algo nada a ver ex: int or float
            raise TypeError("A Data/Hora deve ser um texto (str) ou um objeto datetime.")

    @property
    def status_consulta (self):
        return self.__status_consulta
    
    @status_consulta.setter
    def status_consulta (self, status_recebido):
        if status_recebido is None:
            novo_status = StatusConsulta.AGENDADA
        elif isinstance(status_recebido, StatusConsulta):
            novo_status = status_recebido
        elif isinstance(status_recebido, str):
             try:
                 novo_status = StatusConsulta[status_recebido.upper()]
             except KeyError:
                 try:
                    novo_status = StatusConsulta(status_recebido)
                 except ValueError:
                    raise ValueError(f"Status: '{status_recebido}' é inválido. Use um membro de StatusConsulta.")
        else:
            raise TypeError("O status deve ser do tipo StatusConsulta ou string.") 
            # lembrando aqui só entra c o usuario tentar mandar um int ou float
        self.__status_consulta = novo_status
    

    def adicionar_prescricao (self, prescricao : Prescricao):
        if not isinstance(prescricao, Prescricao):
            raise TypeError("A prescrição deve ser uma instância da classe Prescricao.")
        self.prescricao = prescricao
        self.status_consulta = StatusConsulta.REALIZADA

    def realizar_consulta (self):
        self.status_consulta = StatusConsulta.REALIZADA
        info = f"Consulta de {self.data_hora} finalizada com sucesso."
        return info
    
    def cancelar_consulta (self):
        self.status_consulta = StatusConsulta.CANCELADA
        return
    
    def __str__(self):
        infos = f"\n============= CONSULTA ============="
        infos += f"\nStatus: {self.status_consulta.value}"
        infos += f"\nMédico: {self.medico.nome}"
        infos += f"\nPaciente: {self.paciente.nome}"
        infos += f"\nData e Hora: {self.data_hora.strftime('%d-%m-%Y %H:%M')}"
        valor_final = self.fechar_conta()
        infos += f"\nPagamento: {self.estrategia_pagamento} -> R$ {valor_final:.2f}"
        if self.prescricao:
            infos += f"{self.prescricao.exibir_Exames_Medicamentos()}"
        else:
            infos += f"\nPrescrição: Não informada"
        infos += f"\n====================================="
        return infos
    
    def fechar_conta(self):
        """
        Usa o polimorfismo da estratégia para calcular o valor.
        A Consulta não sabe a regra, ela só pergunta para a estratégia.
        """
        return self.estrategia_pagamento.calcular_valor(self.VALOR_BASE)