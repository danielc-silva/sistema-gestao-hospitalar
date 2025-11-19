from model.Consulta import Consulta
from model.PessoaFactory import PessoaFactory
from model.EstrategiasPagamento import PagamentoConvenio, PagamentoParticular, PagamentoRetorno, PagamentoSUS 
from model.Prescricao import Prescricao
from model.ExameSangue import ExameSangue
from model.ExameRaioX import ExameRaioX


try:
    Medico_1 = PessoaFactory.criar_pessoa("Medico",
                                             nome = "Cláudia Souza Silva", 
                                             cpf = "12345678900", 
                                             data_nascimento = "01-01-1980",
                                             id_funcionario = "MED123",
                                             salario = 12000.00,
                                             status = "ATIVO",
                                             crm = "CRM12345",
                                             especialidade = "Cardiologia"
                                             )

    Enferemeiro_1 = PessoaFactory.criar_pessoa("Enfermeiro",
                                             nome = "Ana Maria Oliveira", 
                                             cpf = "09876543211", 
                                             data_nascimento = "15-05-1985",
                                             id_funcionario = "ENF456",
                                             salario = 8000.00,
                                             status = "ATIVO",
                                             coren = "COREN67890"
                                             )
    
    Paciente_1 = PessoaFactory.criar_pessoa("Paciente",
                                             nome = "Carlos Eduardo Lima",  
                                             cpf = "11223344556",
                                             data_nascimento = "20-10-1990",
                                             id_paciente = "PAC789"
                                             )
    
    Consulta_1 = Consulta(Medico_1, Paciente_1, "25-12-2025 10:00", None, None)
    Consulta_2 = Consulta(Medico_1, Paciente_1, "31-12-2025 09:00", None, PagamentoConvenio("Usamed", 25))
    Consulta_3 = Consulta(Medico_1, Paciente_1, "01-01-2026 11:00", None, PagamentoSUS())
    Consulta_4 = Consulta(Medico_1, Paciente_1, "15-01-2026 14:00", None, PagamentoParticular())
    Consulta_5 = Consulta(Medico_1, Paciente_1, "24-05-2027 09:00", None, PagamentoConvenio("Unimed", 75))

    Prescricao_3 = Prescricao(Medico_1, Paciente_1)
    Prescricao_3.adicionar_medicamento("Dipirona 500mg")
    Prescricao_3.adicionar_medicamento("Amoxicilina 250mg")
    Exame_3 = ExameSangue("Hemograma Completo")
    Prescricao_3.adicionar_exame(Exame_3)

    Consulta_1.realizar_consulta()
    Consulta_2.cancelar_consulta()
    Consulta_3.adicionar_prescricao(Prescricao_3)

    print (Consulta_1)
    print (Consulta_2)
    print (Consulta_3)
    print (Consulta_4)
    print (Consulta_5)

except Exception as e:
        print(f"Erro: {e}")