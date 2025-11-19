from .Exame import Exame
from .Paciente import Paciente

class ExameRaioX (Exame):
    def __init__(self, parte_do_corpo = None):
        super().__init__()
        self.parte_do_corpo = parte_do_corpo

    @property
    def parte_do_corpo (self):
        return self.__parte_do_corpo
    
    @parte_do_corpo.setter
    def parte_do_corpo (self, parte_recebida):
        if (parte_recebida == None):
            raise ValueError ("O campo Parte do Corpo é obrigatório.")
        self.__parte_do_corpo = parte_recebida

    def realizar_exame(self, paciente_alvo : Paciente):
        info = (f"\nTirando Raio-X do ({self.parte_do_corpo}) de {paciente_alvo.nome}")
        return info
    
    def __str__(self):
        infos = f"\nRaio-X [{self.parte_do_corpo}]"
        return infos
    
    
    
