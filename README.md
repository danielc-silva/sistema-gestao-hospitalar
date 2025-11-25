# Sistema de Gestão Hospitalar 

Projeto final desenvolvido para a disciplina de Tecnologia Orientada a Objetos (TOO). O sistema simula o fluxo de atendimento de um hospital, aplicando os pilares da POO e Padrões de Projeto.

## Descrição do Projeto
O sistema permite o cadastro de funcionários e pacientes, agendamento de consultas, realização de atendimentos médicos com prescrição de medicamentos e exames, e gestão de prontuários eletrônicos com acesso restrito.

## Pilares da POO

O projeto foi modelado com base nos 4 pilares fundamentais:

1.  **Abstração:** Utilização de classes abstratas (`Pessoa`, `Funcionario`, `Exame`) para definir contratos e moldes para as entidades concretas.
2.  **Encapsulamento:** Proteção de dados sensíveis. Ex: A lista de histórico no `Prontuario` é privada e só pode ser alterada via método `atualizar_entradas()`, garantindo a integridade dos dados.
3.  **Herança:** Reutilização de código. `Medico` e `Enfermeiro` herdam atributos e métodos comuns de `Funcionario`.
4.  **Polimorfismo:**
    * **Nos Exames:** O método `realizar_exame()` comporta-se de forma diferente para `ExameSangue` e `ExameRaioX`.
    * **Nos Pagamentos:** O método `calcular_valor()` altera o preço final dependendo da estratégia (SUS, Convênio ou Particular).

## Padrões de Projeto (Design Patterns)

### 1. Factory Method (Obrigatório)
Implementado na classe `PessoaFactory`.
* **Objetivo:** Centralizar e desacoplar a criação de objetos complexos. O sistema pede à fábrica "Quero um Médico" e ela devolve o objeto instanciado e validado, sem expor a lógica de criação no código principal.

### 2. Strategy Pattern (Adicional)
Implementado no cálculo de cobrança das Consultas (`EstrategiasPagamento`).
* **Objetivo:** Permitir que a regra de negócio (preço da consulta) mude dinamicamente sem alterar a classe `Consulta`.
* **Estratégias:** `PagamentoParticular`, `PagamentoConvenio` e `PagamentoSUS` (Gratuito).

## Diagrama de Classes UML

![UML do projeto](imagens/UML_Hospitalar.png)

## Como Executar

1.  Certifique-se de ter o Python 3.13 instalado.
2.  Clone o repositório.
3.  Execute o arquivo principal na raiz do projeto:
    ```bash
    python Hospital.py
    ```