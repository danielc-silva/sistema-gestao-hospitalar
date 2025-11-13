# Sistema de Gerenciamento Hospitalar (Projeto TOO)

Projeto da disciplina de Tecnologia de Orientação a Objetos (TOO) para um sistema de gerenciamento hospitalar, focado nos módulos de Agendamento e Prontuários.

## Conceitos Aplicados

Este projeto implementa os 4 Pilares da POO e Padrões de Projeto:

* **Herança:** (Ex: `Pessoa` -> `Funcionario` -> `Medico`)
* **Encapsulamento:** Proteção de dados (ex: `Prontuario` com atributos privados).
* **Abstração:** Classes abstratas como `Funcionario` e `Exame` (`ABC` e `@abstractmethod`).
* **Polimorfismo:** Métodos sobrescritos como `realizar_exame()`.
* **Associação/Composição:** (Ex: `Paciente` "tem um" `Prontuario`).
* **Padrão Factory:** A `FuncionarioFactory` para centralizar a criação de objetos.
