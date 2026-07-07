# Trabalho Final - Célula de Paletização com UR10

**Universidade Federal de Santa Catarina - UFSC/Joinville**
**Disciplina:** EMB5615-09605 (20261) - Robótica e Sistemas Mecatrônicos
**Docente:** Anelize Zomkowski Salvi
**Semestre:** 2026/1

## 👥 Equipe
* **Ítalo Miranda Kusmin Alves** - Matrícula: 22101930
* **Gustavo Moro** - Matrícula: 22101929
* **Bernardo Hott Rocha** - Matrícula: 19102047
* **Elison Maiko Oliveira de Souza** - Matrícula: 22102900

## 🎯 Escopo do Trabalho
O tema geral deste projeto é o desenvolvimento de uma célula didática de paletização utilizando o robô colaborativo UR10. O objetivo é implementar uma solução para a movimentação, organização e manipulação de caixas dentro de um cenário de paletização. A cena mínima deve demonstrar a capacidade de coletar uma caixa, transportá-la até uma posição calculada no pallet, depositá-la e retornar para o próximo ciclo.

Nossa equipe optou pela **Trilha 1**. O escopo desta trilha envolve:
* O desenvolvimento de uma rotina de paletização simulada.
* A execução de uma rotina simples e funcional no robô UR10 real.

*Nota:* Embora a especificação da disciplina sugira o uso do CoppeliaSim para esta trilha, o ambiente de simulação escolhido para o desenvolvimento do nosso projeto foi o **RoboDK**. 

## 📁 Estrutura do Repositório
A organização dos arquivos no repositório reflete as duas frentes principais de desenvolvimento do trabalho:

* 📂 **`/Cena_Minima`**: Contém os scripts (em URScript/Python), arquivos de configuração e a documentação específica para a execução da rotina de paletização no robô UR10 real. Este diretório possui seu próprio README com os detalhes de implementação e testes físicos.
* 📂 **`/RoboDK`**: Contém os arquivos da estação de simulação construída no software RoboDK. Inclui a parametrização do ambiente, geração das posições de deposição e o README específico explicando a lógica da célula virtual.
* 📄 **`Readme.md`**: Este documento atual, apresentando a visão geral do projeto, a equipe responsável e o mapeamento das pastas.