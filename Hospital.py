from model.SistemaAgendamento import SistemaAgendamento
from model.ExameSangue import ExameSangue
from model.ExameRaioX import ExameRaioX
from model.PessoaFactory import PessoaFactory
from model.EstrategiasPagamento import PagamentoConvenio, PagamentoParticular, PagamentoSUS
from model.Prescricao import Prescricao

# O valor base da consulta foi ajustado para 400.00 na classe Consulta.py

try:
    print("\nINICIANDO SISTEMA DE GESTÃO HOSPITALAR...")

    Agenda = SistemaAgendamento() # criando o sistema de agendamento

    print("\nCriando pessoas através da PessoaFactory...")

    Medico_1 = PessoaFactory.criar_pessoa("Medico",
                                            nome = "Jõao Augusto Silva",
                                            cpf = "98765432100",
                                            data_nascimento = "10-10-1975",
                                            id_funcionario = "MED001",
                                            salario = 15000.00,
                                            status = "ATIVO",
                                            crm = "CRM56789",
                                            especialidade = "Ortopedia"
                                            )
    
    Enfermeiro_1 = PessoaFactory.criar_pessoa("Enfermeiro",
                                            nome = "Ana Beatriz Costa", 
                                            cpf = "12345678911",
                                            data_nascimento = "22-03-1980",
                                            id_funcionario = "ENF002",
                                            salario = 9000.00,
                                            status = "ATIVO",
                                            coren = "COREN12345"
                                            )
    
    Paciente_1 = PessoaFactory.criar_pessoa("Paciente",
                                            nome = "Lucas Fernandes",
                                            cpf = "55443322110",
                                            data_nascimento = "05-06-1995",
                                            id_paciente = "PAC003"
                                            )
    
    print("\nMostrando informações das pessoas criadas:")

    print(f"{Medico_1}\n{Enfermeiro_1}\n{Paciente_1}")

    Paciente_1.prontuario.atualizar_entradas(Medico_1, "Paciente apresenta dor lombar intensa após queda.")

    Prescricao_1 = Prescricao(Medico_1, Paciente_1)
    Prescricao_1.adicionar_medicamento("Dipirona 50mg")
    Prescricao_1.adicionar_medicamento("Paracetal 100mg")

    Exame_1 = ExameRaioX("Coluna Lombar")
    Prescricao_1.adicionar_exame(Exame_1)

    Agenda.agendar_consulta("1", Medico_1, Paciente_1, "10-10-2026 09:00", PagamentoConvenio("Usamed", 30))

    print("\nMostrando sistema de agendamento após agendar uma consulta:")
    print(Agenda)

    Agenda.adicionar_prescricao_consulta("1", Prescricao_1) # adicionando prescrição à consulta agendada de acordo com o código

    print("\nMostrando detalhes da consulta agendada após adicionar prescrição:")
    print(Agenda)

    print(f"\nSolicitando que funcionarios trabalhem:{Enfermeiro_1.trabalhar()}\n{Medico_1.trabalhar()}\n")

    Agenda.agendar_consulta("2",Medico_1, Paciente_1, "15-10-2026 11:00", PagamentoParticular())

    Agenda.adicionar_prescricao_consulta("2", Prescricao_1) # adicionando prescrição à consulta agendada de acordo com o código
    print(Agenda)

    



    

    




except Exception as e:
    print(f"Erro: {e}")


