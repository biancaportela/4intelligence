# Série Temporal: projeção de inadimplência

Esse projeto faz parte do primeiro de dois desafios propostos pela  [4intelligence](https://www.4intelligence.ai/) para a vaga de cientista de dados.

O desafio técnico é projetar a taxa de inadimplência dos próximos 12 meses da série de inadimplência da carteira de crédito disponibilizada pelo Banco Central do Brasil, defender a projeção e responder quais são, provavelmente os drivers desses valores.

O resultados da análise, assim como todos os passos e justificativas para minhas decisões podem ser encontradas no JupyterNotebook [aqui](https://github.com/biancaportela/4intelligence/blob/main/case_1/analise_final.ipynb).

A projeção de séries temporais é um tópico particular dentro da ciência de dados. Isso por que, uma série temporal representa uma sequência de observações de uma variável específica ao longo do tempo. Um dos principais objetivos é a previsão dos valores futuros dessa variável. Essa capacidade de previsão é viável devido à persistência parcial dos valores da variável ao longo do tempo - o valor em um determinado período está relacionado aos valores que a variável assumiu em períodos anteriores. Portanto, é possível estabelecer uma correlação entre a variável em estudo e seus valores passados. Portanto, em séries temporais a projeção do futuro é baseada por fatores passados - as defasagens. 

Nessa projeção eu optei por utilizar a modelagem econometrica clássica. Os passos para a projeção foram: entender a base, procurar por valores ausentes e plotar o gráfico da série, fazer a decomposição da série temporal, analisar a estacionariedade, fazer o  modelo (foram testados os modelos ARIMA e SARIMA), avaliar os modelos através de algumas métricas e fazer a projeção para os próximos 12 meses.

Essa série cobre um espaço temporal de mais de 10 anos, inclusive os anos de pandemia da COVID-19. A pandemia afetou o comportamento de diversos mercados e com o mercado de crédito não poderia ser diferente. Isso afeta os valores da projeção obtida. 

Outro problema que encontrei com a série foi que ao fazer o teste de estacionariedade, a série foi considerada estacionária em nível. Por causa disso, continuei com a projeção. Entretanto, os modelos tiveram resultados muito ruins. Na tentativa de melhorar as projeções, eu tirei a primeira diferença da série. Eu desconfiei que o fator de tendência estava afetando meus resultados originais. Após tirada a primeira diferença fiz o mesmo processo e obti resultados melhores. 

Um passo posterior é utilizar modelos mais sofisticados que consigam modelar os anos de pandemia de maneira mais satisfatoria. O [Prophet](https://facebook.github.io/prophet/) é um modelo de previsão de séries temporais desenvolvido pelo Facebook para ajudar na previsão de dados temporais com sazonalidade e mudanças significativas de tendência (como esse caso). 

Além de usar um modelo mais robusto, posso levar em consideração os anos de pandemia de maneira mais explicita no modelo. A documentação do Prophet oferece uma [metodologia](https://facebook.github.io/prophet/docs/handling_shocks.html) para lidar com o choque da pandemia, que é tratar os lockdowns como um feriado único. 

# REFERÊNCIAS

- Inadimplência da carteira de crédito - [Banco Central do Brasil](https://dadosabertos.bcb.gov.br/dataset/21082-inadimplencia-da-carteira-de-credito---total) 

- Econometria na Prática - Cláudia Malbouisson, Gisele F. Tiryaki

- Time Series Analysis using Python - [Learnerea](https://www.youtube.com/watch?v=O5pataOw33Y&list=PLnUZAWEqDL-lHkz1GmaTUL71RxZaA_sbq&index=54)

- Séries Temporais com Prophet - Análise e previsão de dados com Python, Allan Spadini e Valquíria Alencar

- Handling Shocks -  [Documentação Prophet](https://facebook.github.io/prophet/docs/handling_shocks.html)

