# Dicionário de dados

- Este dataset contém informações sobre pagamentos inadimplentes, fatores demográficos, dados de crédito, histórico de pagamentos e extratos de faturas de clientes de cartões de crédito em Taiwan de abril de 2005 a setembro de 2005.

- Há linhas 30000 e 25 colunas

- O dataset foi atualizado pela última vez há 7 anos atrás

# Descrição das colunas

Aqui está a tradução do dicionário em formato Markdown:

- `ID`: ID de cada cliente

- `LIMIT_BAL`: Valor do crédito concedido em dólares taiwaneses (inclui crédito individual e familiar/suplementar)
- `SEX`: Gênero (1=masculino, 2=feminino)
- `EDUCATION`: (1=pós-graduação, 2=universidade, 3=ensino médio, 4=outros, 5=desconhecido, 6=desconhecido)
- `MARRIAGE`: Estado civil (1=casado, 2=solteiro, 3=outros)
- `AGE`: Idade em anos
- `PAY_0`: Estado de pagamento em setembro de 2005 (-1= pagamento em dia, 1= atraso de um mês no pagamento, 2= atraso de dois meses no pagamento, … 8= atraso de oito meses no pagamento, 9= atraso de nove meses ou mais no pagamento)
- `PAY_2`: Estado de pagamento em agosto de 2005 (escala igual à acima)
- `PAY_3`: Estado de pagamento em julho de 2005 (escala igual à acima)
- `PAY_4`: Estado de pagamento em junho de 2005 (escala igual à acima)
-`PAY_5`: Estado de pagamento em maio de 2005 (escala igual à acima)
- `PAY_6`: Estado de pagamento em abril de 2005 (escala igual à acima)
- `BILL_AMT1`: Valor do extrato da fatura em setembro de 2005 (dólar taiwanês)
- `BILL_AMT2`: Valor do extrato da fatura em agosto de 2005 (dólar taiwanês)
- `BILL_AMT3`: Valor do extrato da fatura em julho de 2005 (dólar taiwanês)
- `BILL_AMT4`: Valor do extrato da fatura em junho de 2005 (dólar taiwanês)
- `BILL_AMT5`: Valor do extrato da fatura em maio de 2005 (dólar taiwanês)
-`BILL_AMT6`: Valor do extrato da fatura em abril de 2005 (dólar taiwanês)
-`PAY_AMT1`: Valor do pagamento anterior em setembro de 2005 (dólar taiwanês)
-`PAY_AMT2`: Valor do pagamento anterior em agosto de 2005 (dólar taiwanês)
-`PAY_AMT3`: Valor do pagamento anterior em julho de 2005 (dólar taiwanês)
-`PAY_AMT4`:Valor do pagamento anterior em junho de 2005 (dólar taiwanês)
- `PAY_AMT5`:Valor do pagamento anterior em maio de 2005 (dólar taiwanês)
- `PAY_AMT6`:Valor do pagamento anterior em abril de 2005 (dólar taiwanês)
- `default.payment.next.month`: Pagamento padrão (1=sim, 0=não)