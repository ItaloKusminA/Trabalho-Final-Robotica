# Cena Mínima - Execução no UR10 (Real e URSim10)

Este diretório contém os códigos-fonte necessários para a execução da rotina paramétrica de paletização. A lógica desenvolvida aqui atende aos requisitos da cena mínima da Trilha 1 e foi amplamente testada e validada no simulador **URSim10** antes de ser implantada e executada no robô UR10 real.

## 📄 Descrição dos Arquivos

A solução é composta por dois arquivos principais que trabalham em conjunto: o código de movimentação do robô e o script de envio de dados pela rede.

### 1. `pallet.script` (Lógica de Paletização em URScript)
Este arquivo contém a função `pallet_parametric()`, que é o "cérebro" da operação. Ele é executado diretamente na controladora do robô (ou no URSim10) e possui as seguintes características:
* **Parametrização:** A organização das caixas não utiliza posições fixas gravadas manualmente. O código interpola as posições de deposição com base em 4 pontos de referência (os cantos do pallet: `Pallet1` a `Pallet4`).
* **Matriz de Deposição:** O script está configurado para uma grade de 5 colunas por 5 linhas, totalizando 25 caixas dispostas em 1 camada (`grid_cols = 5`, `grid_rows = 5`, `grid_layers = 1`).
* **Trajetória de Segurança:** Inclui pontos de aproximação (`approach_pose`) e recuo (`exit_pose`) com uma distância segura de 150 mm (`approach_dist = 0.150`), garantindo que o robô não colida com as caixas já posicionadas.
* **Validação de Limites:** Utiliza a função `is_within_safety_limits()` para checar se a cinemática de todos os pontos gerados matematicamente está dentro do envelope de segurança antes de realizar qualquer movimento (`movel`).
* **Acionamento da Garra:** O acionamento da ferramenta de pega (ou sua simulação) é feito através da Porta Digital 0 (`set_standard_digital_out(0, True/False)`).

### 2. Script de Envio via TCP/IP (Python)
Script desenvolvido em Python responsável por ler o arquivo `pallet.script` e enviá-lo diretamente para a controladora do robô através de uma conexão Socket.
* O script conecta-se ao endereço IP do robô (`192.168.0.10`).
* Utiliza a porta padrão `30002` da Universal Robots para enviar comandos URScript em tempo de execução.

## 🚀 Como Executar

### Pré-requisitos
* Ter o Python 3.x instalado na máquina.
* Estar conectado à mesma rede local que o robô UR10 ou estar com o simulador URSim10 rodando na máquina/máquina virtual correspondente.

### Passo a passo
1. Certifique-se de que o robô físico ou o URSim10 esteja ligado e configurado com o IP `192.168.0.10` (caso o IP seja diferente, atualize a variável `ROBOT_IP` no script Python).
2. Deixe o arquivo `pallet.script` no mesmo diretório do script Python.
3. No terminal, execute o script Python:
   ```bash
   python nome_do_script_python.py