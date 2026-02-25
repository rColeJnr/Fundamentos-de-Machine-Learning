# 🤖 Introdução ao Scikit-learn e Regressão Linear

Neste módulo, aprenderemos como construir modelos de **Regressão**. Focaremos exclusivamente na **Regressão Linear** para entender os fundamentos antes de avançarmos para técnicas mais complexas.

---

## 📚 O que é o Scikit-learn?

O **Scikit-learn** fornece uma API extensa para ajudar a realizar tarefas de Machine Learning (ML). De acordo com o site oficial:

> "Scikit-learn é uma biblioteca de machine learning de código aberto que suporta aprendizagem supervisionada e não supervisionada. Também fornece várias ferramentas para ajuste de modelos, pré-processamento de dados, seleção e avaliação de modelos, entre outras utilidades."

Neste curso, utilizaremos o Scikit-learn para construir modelos de **Machine Learning Tradicional**. Evitaremos deliberadamente redes neurais e *Deep Learning*, pois estes tópicos exigem uma base sólida que construiremos aqui primeiro.

---

## 📉 O que é Regressão?

Existem muitos tipos de métodos de regressão, e a escolha depende da resposta que você procura:

1.  **Regressão Linear:** Utilizada quando você procura um **valor numérico**. 
    * *Exemplo:* Prever a altura provável de uma pessoa com base na sua idade.
2.  **Regressão Logística:** Utilizada quando você procura uma **atribuição de categoria**. 
    * *Exemplo:* Descobrir se um prato é considerado vegano ou não (Sim/Não).
3. **Regressão Linear Múltipla** Utilizada quando você quer prever um valor numérico usando duas ou mais variáveis explicativas.
    * *Exemplo:* Prever o preço de revenda de um carro com base no ano de fabricação, quilometragem e potência do motor.
5. **Regressão Random Forest (Floresta Aleatória)** Utilizada quando se busca alta precisão, combinando o resultado de várias árvores de decisão para chegar a um consenso.
    * *Exemplo:* Prever o tempo de vida útil restante de uma turbina de avião com base em sensores de vibração, calor e pressão.

---

## 🧪 Projeto Prático:  Conjunto de Dados de california housing

Vamos colocar as mãos na massa utilizando um Jupyter Notebook e um conjunto de dados real sobre precos de imoveis, que já vem incluído no Scikit-learn para fins de aprendizado.