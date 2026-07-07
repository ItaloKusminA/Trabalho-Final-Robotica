# Simulação de Paletização com Esteira - RoboDK 🤖📦

Projeto de simulação de paletização desenvolvido no RoboDK, integrando rotinas de robótica industrial com scripts em Python para automatizar a criação de pallets de forma escalável.

## 🛠️ Softwares e Objetos Utilizados

* **Software:** RoboDK (versão 6.0.5)
* **Linguagem Auxiliar:** Python (API nativa do RoboDK)
* **Elementos da Cena:** Todos os modelos 3D utilizados (braço robótico UR10, garra a vácuo, mesas, caixas de papelão, esteira e pallet) foram importados diretamente da **Biblioteca Online do RoboDK**, garantindo a precisão das dimensões industriais.

---

## ⚙️ Arquitetura e Lógica do Projeto

A principal vantagem desta simulação é a eliminação do ensino manual (*teach*) para cada posição do pallet. A automação foi estruturada em três frentes principais:

### 1. Rotina Base de Movimento (`Prog1`)
Foi criado um subprograma gráfico diretamente no RoboDK contendo a instrução de *Pick and Place* para apenas **uma caixa**. O robô aproxima da esteira, coleta o item e o deposita na coordenada inicial do pallet.

### 2. Automação e Expansão da Grade (`palletizar.py`)
Para preencher o pallet completo, utilizamos este script em Python que atua como o cérebro da operação. Ele é responsável por:
* **Animação da Esteira:** O script clona a caixa original (molde) no fundo da esteira e cria uma animação de deslocamento contínuo até que a caixa chegue ao ponto de coleta.
* **Cálculo da Matriz:** Com base nas dimensões físicas da caixa, o código calcula matematicamente os *offsets* (deslocamentos). O incremento no **Eixo X** forma as colunas, no **Eixo Y** forma as linhas, e no **Eixo Z** constrói as camadas.
* **Execução Dinâmica:** A cada nova iteração, o script atualiza as coordenadas do alvo final (*Place*) no espaço 3D e aciona o `Prog1`. O robô executa o mesmo movimento base, mas soltando a caixa em um local novo e milimetricamente calculado.

### 3. Restauração do Ambiente (`restart.py`)
Para evitar que o usuário precise apagar dezenas de caixas manualmente ao final da simulação, este script de limpeza foi criado. Com um único clique, ele:
* Varre a árvore do projeto e deleta todos os clones de caixas gerados pelo programa principal.
* Reseta os alvos de destino (*Targets*) para suas coordenadas originais.
* Retorna o manipulador robótico de forma segura para sua posição inicial (*Home*), deixando a célula pronta para um novo ciclo.

---

## 🚀 Como Executar

1. Abra o arquivo `.rdk` contido nesta pasta no RoboDK.
2. Na árvore de projetos (lateral esquerda), dê um duplo clique no script **`restart`** para garantir que a cena está limpa e na posição inicial.
3. Em seguida, dê um duplo clique no script **`palletizar`** para iniciar a simulação contínua com a esteira e o empilhamento automático.