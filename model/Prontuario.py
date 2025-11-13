from datetime import date, time, datetime, timedelta
from .Paciente import Paciente

class Prontuario ():
    def __init__ (self, paciente : Paciente):
        self.paciente = paciente
        self.__entrada = []

    # medico recebe ou objeto do tipo Medico 
    def adicionar_entrada (self, medico : Medico, descrição = None):
        if (descrição == None):
            raise ValueError ("\nCampo descrição é obrigatório")
        texto = ''
        dados_entrada =  {
            "data": datetime.now(),
            #"medico": medico.(criaar algo pra buscar o nome do médico, na class médico)
            "descricao": texto }
# Conferir essa classe tá estranho vou criar as demais primeiro