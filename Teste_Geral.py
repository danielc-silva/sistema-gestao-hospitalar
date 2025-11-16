from model.Pessoa import Pessoa
from model.Funcionario import Funcionario
from model.Medico import Medico
from model.Enfermeiro import Enfermeiro
from model.Paciente import Paciente
from model.ExameSangue import ExameSangue
from model.ExameRaioX import ExameRaioX
from model.Prescricao import Prescricao

p3 = Paciente("Daniel cipriano da silva", "04039434952", "14-12-2005", "ddsf234")
E1 = Enfermeiro("Maria Anônia", "98763456787", "12-08-2000", "321321", 10000, "ativo", "9999-RS")
print(p3)
M1 = Medico ("João Silva", "98763456787", "12-08-2000", "321321", 10000, "ativo", "1234-RS", "Cardiologista")
M2 = Medico ("Gustavo Marques", "98763456787", "12-08-2000", "321321", 10000, "ativo", "1234-RS", "Cardiologista")
M2.afastar_funcionario()
M2.ativar_funcionario()
E1.afastar_funcionario()
E1.ativar_funcionario()
E1.aviso_previo_funcionario()
E1.desligar_funcionario()
print(f"\n{E1.trabalhar()}")
print(E1)
p3.prontuario.atualizar_entradas(M1, "Torção no joelho esquerdo e possível fratura no femur direito.")
p3.prontuario.atualizar_entradas(M2, "Dificuldade de respiração.")
print (f"{p3.prontuario.mostrar_prontuario()}")
print (M2)
print(M2.mostrar_historico())
print(E1.mostrar_historico())
exame1 = ExameSangue("Hemograma Completo")
print(exame1.realizar_exame(p3))
exame2 = ExameRaioX("Tórax")
print(exame2.realizar_exame(p3))
print(M2.trabalhar())
print("\n")
presc1 = Prescricao(M1, p3)
presc1.adicionar_exame(exame1)
presc1.adicionar_exame(exame2)
presc1.adicionar_medicamento("Paracetamol 500mg")
presc1.adicionar_medicamento("Ibuprofeno 400mg")
print(presc1)
print(presc1.realizar_exames())