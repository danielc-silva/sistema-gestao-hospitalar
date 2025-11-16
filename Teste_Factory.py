from model.FuncionarioFactory import FuncionarioFactory

Medico_1 = FuncionarioFactory.criar_funcionario("Medico",
                                             nome = "Cláudia Souza Silva", 
                                             cpf = "12345678900", 
                                             data_nascimento = "01-01-1980",
                                             id_funcionario = "MED123",
                                             salario = 12000.00,
                                             status = "ATIVO",
                                             crm = "CRM12345",
                                             especialidade = "Cardiologia"
                                             )

Enferemeiro_1 = FuncionarioFactory.criar_funcionario("Enfermeiro",
                                             nome = "Ana Maria Oliveira", 
                                             cpf = "09876543211", 
                                             data_nascimento = "15-05-1985",
                                             id_funcionario = "ENF456",
                                             salario = 8000.00,
                                             status = "ATIVO",
                                             coren = "COREN67890"
                                             )

print(Medico_1)
print(Enferemeiro_1)