# 🎬 Projeto de Curso: Preditor da Avaliação de Anime

Este projeto prático foi desenhado para ensinar o fluxo fundamental de Ciência de Dados. Construiremos um sistema que prevê a nota dos usuários (0.0 - 10.0) de um anime no MyAnimeList (MAL) utilizando dados atualizados de 2025.

---

Com este projecto podera entender melhor como trabalhar com dados, como na base dos seus dados escolher o modelo para os seus dados, como preparar os dados para o modelo e por fim, como apresentar um modelo ao usuario (inference)!

---

## 🛤️ O Roteiro de Aprendizagem

Para manter o aprendizado focado e eficiente, dividiremos o trabalho em três etapas claras:

### 1. Limpeza de Dados 🧹
Dados brutos costumam ser "sujos". Começaremos com o dataset original do Kaggle e faremos o seguinte:
- **Tratamento de valores ausentes:** Identificar e tratar falta de informacao no dataset.
- **Conversão de dados:** Transformar colunas de texto em números que o computador consiga processar. Formatar colunas de dados em um formato que o modelo consigo usar para aprender devidamente.
- **Filtragem:** Remover informacao irrelevante do dataset.

**Objetivo:** Gerar um arquivo CSV "limpo" e pronto para o modelo.

---

### 2. Análise Exploratória (EDA - Exploratory Data Analysis) 📊
Antes de aplicar matemática, precisamos entender os padrões visuais e estatísticos:
- **Análise de Correlação:** Será que o número de episódios realmente afeta a avalição final?
- **Distribuição de Gêneros:** Quais categorias (Ação, Romance, Isekai) costumam ser mais bem avaliadas?
- **Visualização:** Criação de gráficos para validar nossas hipóteses sobre os dados.

---

### 3. Modelagem com Regressão Linear 🤖
Neste projeto, utilizaremos a Regressão Linear como nossa ferramenta principal por sua clareza e simplicidade.
- **Conceito:** Aprenderemos como o modelo encontra a relação matemática entre as características (gênero, episódios, rating) e a nota final.
- **Avaliação:** Usaremos o MAE (Erro Médio Absoluto) para medir, em média, quantos pontos o nosso "chute" erra em relação à nota real.
- **Prática:** Veremos como o Scikit-Learn executa o treinamento com poucas linhas de código.

---

## 📊 Métricas de Performance Esperadas
Ao final, seu modelo deverá atingir resultados próximos a estes:

`MAE ≈ 0.44 pontos`

---

## 🛠️ Tecnologias Utilizadas
- **Python:** Linguagem de programação.
- **Pandas & NumPy:** Ferramentas essenciais para manipulação e limpeza de tabelas.
- **Scikit-Learn:** Biblioteca principal para criação e avaliação do modelo de Regressão Linear.
- **Matplotlib & Seaborn:** Para a geração de gráficos e visualizações.
- **Streamlit:** Para criar a interface web interativa onde o usuário poderá testar o preditor.
