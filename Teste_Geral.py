from model.Pessoa import Pessoa
from model.Funcionario import Funcionario
from model.Medico import Medico
from model.Enfermeiro import Enfermeiro
from model.Paciente import Paciente

p3 = Paciente("Daniel cipriano da silva", "04039434952", "14-12-2005", "ddsf234")

print(p3)

M1 = Medico ("João Silva", "98763456787", "12-08-2000", "321321", 10000, "ativo", "1234-RS", "Cardiologista")
M2 = Medico ("Gustavo Marques", "98763456787", "12-08-2000", "321321", 10000, "ativo", "1234-RS", "Cardiologista")
M2.afastar_funcionario()
M2.ativar_funcionario()
#p3.afastar_funcionario()
#p3.ativar_funcionario()
#p3.aviso_previo_funcionario()
#p3.desligar_funcionario()
#print(f"\n{p3.trabalhar()}")


p3.prontuario.atualizar_entradas(M1, "Torção no joelho esquerdo e possível fratura no femur direito.")
p3.prontuario.atualizar_entradas(M2, "Dificuldade de respiração.")


print (f"{p3.prontuario.mostrar_prontuario()}")

print (M1)

print("\n")
#print (p3.mostrar_prontuario())


#lembrar de trocar o id funcionario como uma classe abstrata onde em medico tem crm e em enfermeiro tem coren 