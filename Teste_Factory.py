from model.PessoaFactory import PessoaFactory

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

     print(Medico_1)
     print(Enferemeiro_1)
     print(Paciente_1)
     print("\n")

except Exception as e:
        print(f"Erro ao criar pessoa: {e}")