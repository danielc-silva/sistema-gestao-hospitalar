from model.Pessoa import Pessoa
from model.Paciente import Paciente
from model.Funcionario import Funcionario
from model.Medico import Medico
from model.Enfermeiro import Enfermeiro

p3 = Enfermeiro("Daniel cipriano da silva", "04039434952", "14-12-2005", "ddsf234", 10000, None, "12234-RJ")

print(p3)

p3.afastar_funcionario()
p3.ativar_funcionario()
p3.aviso_previo_funcionario()
p3.desligar_funcionario()
print(f"\n{p3.trabalhar()}")

print("\n")
print (p3.mostrar_historico())
