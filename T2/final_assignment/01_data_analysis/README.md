# Cryptocurrencies datasets analysis


## Elliptic dataset

Composto por transações anônimas do *blockchain* da criptomoeda *Bitcoin*. O conjunto de dados possui o formato de um grafo de transações onde cada nó representa uma transação. As arestas, por sua vez, representam o fluxo da criptomoeda.

O conjunto de dados possui 203.769 nós e 234.355 arestas, sua composição de exemplos pode ser observada na figura abaixo. Utilizou-se neste trabalho a porção rotulada do conjunto de dados (22.8%), onde 4.545 transações são rotulados como ilícitas e 42.019 como lícitas. A proporção de exemplos ilícitos para lícitos é de aproximadamente 1:10 caracterizando um conjunto de dados desbalanceado. Todo conjunto de dados é majoritariamente numérico.


![](/01_elliptic_dataset/figs/classes_proportions_1.png)


A descrição das características não está presente devido à proteção intelectual. No entanto as primeiras 94 colunas de características são informações locais da transação, presentes no *blockchain* como o id da transação, entradas e saídas, volume de saída e taxa da transação. As demais 72 características foram agregadas utilizando as informações das transação anterior e posterior a partir de uma transação central e contém o desvio padrão e coeficientes de correlação das transações vizinhas que utilizam as mesmas informações como entradas, saídas, taxa da transação, entre outras.

Para coleta do conjunto de dados foi considerado 49 intervalos de tempo consecutivos. A figura abaixo mostra a distribuição de exemplos lícitos e ilícitos em cada intervalo de tempo fixo presente no mesmo. Nota-se que a quantidade de exemplos ilícitos é pequena em alguns casos.


![](/01_elliptic_dataset/figs/classes_by_timestep.png)


- Que tipos de dados você tem, majoritariamente (atributos numéricos, textuais)?
Majoritamente numéricos.

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 46564 entries, 0 to 46563
Columns: 165 entries, 1 to 165
dtypes: float64(164), int64(1)
memory usage: 58.6 MB
```

- Qual seu objetivo com esse dataset?
Validar sua utilização para detectar transferências de natureza ilegais de bitcoins. 

- Seu dataset é rotulado de que maneira?
O dataset possui duas clases, no entanto grande parte das transações não são rotuladas.

```
Class: 2, Count: 42019, Percentage: 90.239
Class: 1, Count: 4545, Percentage: 9.761

```


- Quais colunas/atributos você julga ser interessante manter e remover? Por quê?
O dataset possui colunas com dados agregados (dados obtidos a partir dos dados originais). Esses dados poderiam ser retirados, pois suas descrições são omitidas por direitos autorais.
