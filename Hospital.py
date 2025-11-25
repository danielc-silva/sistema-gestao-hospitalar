from model.SistemaAgendamento import SistemaAgendamento
from model.ExameSangue import ExameSangue
from model.ExameRaioX import ExameRaioX
from model.PessoaFactory import PessoaFactory
from model.EstrategiasPagamento import PagamentoConvenio, PagamentoParticular, PagamentoSUS
from model.Prescricao import Prescricao

# O valor BASE da consulta foi ajustado para 400.00 na classe Consulta.py

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

    #Medico_1.afastar_funcionario()# afastando médico não é possivel agendar nada com ele

    Paciente_1.prontuario.atualizar_entradas(Medico_1, "Paciente apresenta dor lombar intensa após queda.")

    Prescricao_1 = Prescricao(Medico_1, Paciente_1) # Prescrição criada
    Prescricao_1.adicionar_medicamento("Dipirona 50mg") # Adicionando medicamentos na prescrição
    Prescricao_1.adicionar_medicamento("Paracetal 100mg")

    Exame_1 = ExameRaioX("Coluna Lombar") # Criando exame de Raio X
    Prescricao_1.adicionar_exame(Exame_1) # Adicionando exame na prescrição

    Agenda.agendar_consulta("1", Medico_1, Paciente_1, "10-10-2026 09:00", PagamentoConvenio("Usamed", 30))

    print("\nMostrando sistema de agendamento após agendar uma consulta:")
    print(Agenda)

    Agenda.adicionar_prescricao_consulta("1", Prescricao_1) # adicionando prescrição à consulta agendada de acordo com o código da consulta

    print("\nMostrando detalhes da consulta agendada após adicionar prescrição:")
    print(Agenda)

    print(f"\nSolicitando que funcionarios trabalhem:{Enfermeiro_1.trabalhar()}\n{Medico_1.trabalhar()}\n")

    Agenda.agendar_consulta("2",Medico_1, Paciente_1, "15-10-2026 11:00", PagamentoParticular())

    Agenda.adicionar_prescricao_consulta("2", Prescricao_1) # adicionando prescrição à consulta agendada de acordo com o código

    print(Agenda)

    print (f"\n{Medico_1.nome} é {Medico_1.papel_da_pessoa()} no hospital.")
    print (f"\n{Enfermeiro_1.nome} é {Enfermeiro_1.papel_da_pessoa()} no hospital.")
    print (f"\n{Paciente_1.nome} é {Paciente_1.papel_da_pessoa()} no hospital.")

    Medico_1.ferias_funcionario()
    Medico_1.aviso_previo_funcionario()
    Medico_1.desligar_funcionario()
    print (f"{Medico_1.mostrar_historico()}")

    print (f"{Exame_1.realizar_exame(Paciente_1)}\n") # aqui estou realizando o exame no paciente passado 

    print (f"{Paciente_1.prontuario.mostrar_prontuario()}") # mostrando prontuário do paciente

    Paciente_1.prontuario.atualizar_entradas(Medico_1, "Queixa de dores fortes na coluna.") 
    # vai mostrar mensagem de erro pois o medico se encontra desligado

    Medico_1.ativar_funcionario() # reativando o médico

    Paciente_1.prontuario.atualizar_entradas(Medico_1, "Reclama de dores fortes na coluna.")
    # agr vai atualizar normalmente pois o médico está ativo e pode trabalhar

    print (f"{Paciente_1.prontuario.mostrar_prontuario()}\n")

except Exception as e:
    print(f"Erro: {e}")


