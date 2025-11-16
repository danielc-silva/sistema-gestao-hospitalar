from .Exame import Exame
from .Paciente import Paciente

class ExameSangue (Exame):
    def __init__(self, tipo = None):
        super().__init__()
        self.tipo = tipo

    @property
    def tipo (self):
        return self.__tipo  
    
    @tipo.setter
    def tipo (self, tipo_recebido):
        if (tipo_recebido == None):
            raise ValueError ("O campo Tipo de Exame é obrigatório.")
        self.__tipo = tipo_recebido.upper()

    def realizar_exame(self, paciente_alvo : Paciente):
        info = (f"\nColetando sangue de {paciente_alvo.nome} para exame do tipo ({self.tipo})")
        return info
    
    def __str__(self):
        infos = f"\nExame de Sangue [{self.tipo}]"
        return infos

  