from abc import ABC, abstractmethod


class EstrategiaPagamento(ABC):
    @abstractmethod
    def calcular_valor(self, valor_base: float) -> float:
        pass
    @abstractmethod
    def __str__(self):
        pass


class PagamentoParticular(EstrategiaPagamento):
    def calcular_valor(self, valor_base: float):
        return valor_base # Sem desconto
    
    def __str__(self):
        return "Particular (Valor Integral)"


class PagamentoConvenio(EstrategiaPagamento):
    def __init__(self, nome_convenio, desconto_percentual):
        self.nome_convenio = nome_convenio
        # aqui recebe o percentual, no caso 0.2 é 20%
        self.fator_pagamento = 1.0 - desconto_percentual 

    def calcular_valor(self, valor_base: float):
        return valor_base * self.fator_pagamento
    
    def __str__(self):
        return f"Convênio {self.nome_convenio}"


class PagamentoRetorno(EstrategiaPagamento):
    def calcular_valor(self, valor_base: float):
        return 0.0 # Gratuuito pois é o retorno 
    
    def __str__(self):
        return "Retorno (Gratuito)"
    

class PagamentoSUS(EstrategiaPagamento):
    def calcular_valor(self, valor_base: float):
        return 0.0 # Gratuuito pois é o sus 
    
    def __str__(self):
        return "SUS (Sistema Único de Saúde - Gratuito)"
    

# posso criar mais métodos de pagamento futuramente 
# seguindo essa mesma estrutura sem alterar nada 
# nas outras classes nesse caso a consulta