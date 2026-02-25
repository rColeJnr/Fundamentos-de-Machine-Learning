# 🚀 Guia de Configuração: Machine Learning & Jupyter

 Este guia serve para ajudar com a instalacao e configuraco da sua maquina para rodar models de machine learning.

---

## 🛠️ Fase 1: A Fundação (Python)


### 1. Drivers de GPU 
Certifique-se de atualizar o driver do seu GPU, se tiver.

### 2. Gerenciamento de Pacotes: Miniconda
Esqueça o instalador padrão do Python. O **Miniconda** é a versão leve do Anaconda e o padrão ouro para ML.
* **Download:** [Instalador do Miniconda](https://docs.conda.io/en/latest/miniconda.html).
* **Vantagem:** Ele gerencia bibliotecas complexas (C++, CUDA) que o `pip` às vezes ignora.

---

## 🏗️ Fase 2: Criando seu Workspace

### 1. Criar um Ambiente Virtual
Sempre crie um ambiente novo para cada projeto. No terminal:

```bash
# Cria o ambiente com Python 3.11
conda create -n ml_env python=3.11
conda activate ml_env
```
*
### 2. Instalar as Bibliotecas Essenciais
A maioria dos projetos de ML começa com estes pilares:
- **NumPy**: Para calculos matematicos e arrays.
- **Pandas**: Para manipulacao de tabelas de dados.
- **Scikit-Learn**: Para modelos de ML tradicionais (regressão, árvores, etc.).

```
Bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

### 3. Escolha o seu "sabor" de Deep Learning:
Ou use ambos!
- **PyTorch**: favorito na pesquisa e cada vez mais popular na indústria
 - ```pip install torch torchvision torchaudio```
- **TensorFlow**: favorito parap rodução em larga escala
 - ```pip install tensorflow```
 
##  Fase 3: Guia Rápido de Jupyter Notebook
O Jupyter é onde 90% da ciência de dados acontece. Ele permite misturar código, fórmulas matemáticas e visualizações em um só lugar.
### 1. Instalação e Execução
Dentro do seu ambiente ativo (ml_env):
``` 
Bash
pip install notebook
jupyter notebook
```
Isso abrirá um painel no seu navegador. Crie um novo notebook "Python 3"
### .2. Atalhos Essenciais (Produtividade
| Atalho          | Ação                                                    |
|-----------------|---------------------------------------------------------|
| Shift + Enter   | Executa a célula e vai para a próxima                 |
| Alt + Enter     | Executa a célula e insere uma nova abaixo             |
| Esc + A         | Insere célula acima (Above)                            |
| Esc + B         | Insere célula abaixo (Below)                            |
| Esc + D + D     | Deleta a célula selecionada                            |
| Esc + M         | Muda a célula para Markdown (para notas e textos)     |

### 3. Por que usar o Jupyter?
- **Código Iterativo**: Você pode carregar um dataset pesado uma única vez e ficar experimentando modelos em células diferentes sem precisar recarregar tudo.

- **Visualização**: Gráficos do matplotlib ou seaborn aparecem logo abaixo do código que os gerou.