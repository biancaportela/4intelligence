# Modelo de Classificação para Previsão de Inadimplência em Crédito

![](https://storage.googleapis.com/kaggle-datasets-images/306/666/d68d599bfe6995fa5772df1e82c4e83c/dataset-cover.jpg)


Nos mercados de crédito, um desafio sempre presente é a avaliação da inadimplência. Em um mundo onde a concessão de crédito é essencial para o crescimento econômico e financeiro, a capacidade de prever com precisão se um indivíduo cumprirá suas obrigações financeiras ou se tornará inadimplente é de suma importância.A inadimplência pode ter impactos significativos na estabilidade econômica e nas estratégias de tomada de decisão financeira das famílias e, por consequência, na economia como um todo. Para as empresas de crédito, ter um modelo de classificação para prever se o cliente irá pagar ou não permite gerenciar riscos financeiros, reduzir perdas, tomar decisões de crédito mais informadas, melhorar a experiência do cliente, cumprir regulamentações e aumentar a eficiência operacional. Ao identificar previamente os clientes com maior probabilidade de não pagar suas dívidas, essas empresas podem implementar medidas proativas, como ajustar limites de crédito, taxas de juros e estratégias de cobrança, resultando em uma redução de perdas, melhoria na rentabilidade e na confiança do mercado.

Neste estudo, exploro a construção de um modelo de classificação, utilizando técnicas de machine learning, para prever a probabilidade de inadimplência com base em informações disponíveis de crédito sobre os clientes. 

A base de dados contém informações sobre pagamentos inadimplentes, fatores demográficos, dados de crédito, histórico de pagamentos e extratos de faturas de clientes de cartões de crédito em Taiwan de abril de 2005 a setembro de 2005. O projeto foi desenvolvido em um Jupyter Notebook. Nele encontra-se toda a análise e a justificativa para cada passo tomado. Abaixo, encontra-se links com a fonte dos dados, o dicionário e o notebook da análise.

- [Base de dados]()
- [Dicionário]()
- [Análise]()

O estudo de caso foi feito seguindo a metodologia CRISP-DM. O CRISP-DM é um modelo padrão que define um processo estruturado e organizado para projetos de análise de dados. O modelo é composto por cinco fases: Planejamento, Preparação, Modelagem, Avaliação e Implantação. As medidas para cada etapa foram as seguintes:

1. **Planejamento**: o objetivo da análise foi proposto pela empresa 4intelligence ("Nos mercados de crédito, um problema típico é saber se, dadas as 
informações de uma pessoa, ela pagará ou não sua dívida. A partir da base disponível gere um modelo preditivo de classificação separe 30% da base para teste e traga métricas para validar o modelo em questão"). Escrevi um breve parágrafo sobre a importância desse tipo de projeto, defini as metas dos projeto e identifiquei os recursos necessários para a análise.

2. **Preparação**: a preparação dos dados envolve a coleta e limpeza de dados, a descrição e exploração da base de dados e por fim, a preparação para a modelagem. Durante essa etapa chequei os dados ausentes, se havia ou não dados duplicados, plotei gráficos para entender como as distribuições das variáveis se comportam, eliminei outliers, separei a variável target do resto do dataset, separei em treino e teste e, por fim, realizei o One Hot Encoding nas variáveis qualitativas e a normalização. 

3. **Modelagem**: Na fase de modelagem são escolhidos os modelos para a classificação e eles são avaliados através de algumas métricas. Este caso de classificação é um problema com classes desbalanceadas, por causa disso foi necessário fazer uma etapa de resampling dos dados. Com um primeiro modelo escolhido, fiz a otimização dos hiperparâmetros utilizando o RandomSearch e novamente avaliei os resultados através das métricas escolhidas. De maneira a entender melhor o comportamento do modelo, também plotei os gráficos da matriz de confusão, da curva ROC e a importância das features.

4. **Implementação**: Com o modelo escolhido e otimizado realizei as previsões. 


Como passos futuros, acredito que seja possível melhorar as métricas de desempenho do modelo, principalmente em relação a precisão média. É necessário testar mais modelos e talvez fazer alguma engenharia de atributos. Além disso, um próximo passo seria fazer o deploy deste modelo. O Streamlit é uma biblioteca que facilita a criação de aplicativos da web interativos para análise de dados, visualização e prototipagem rápida. Com o Streamlit é possível criar um site onde o usuário pode fornecer algumas informações e conseguir o resultado da previsão de maneira rápida e simples. Assim, o próximo passo desse projeto seria fazer o deploy do modelo treinado e criar uma plataforma onde possa-se inserir os dados e obter a previsão se o cliente será inadimplente ou não. 
