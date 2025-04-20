# Data Science for dummies

## Pandas

Pandas é uma biblioteca Python desenvolvida para análise e manipulação de dados. O nome "Pandas" deriva de "Panel Data", um termo da econometria para conjuntos de dados multidimensionais.

### Função do pandas
- Permite importar dados de diversos formatos (Excel,CSV, SQL, etc.)
- Oferece estruturas para limpeza e transformação de dados.
- Facilita a análise exploratória dos dados.
- Prepara os dados para modelagem estatística e machine learning.

### O que é um DataFrame?

Um DataFrame é como uma tabela bidimensional no Excel, mas dessa vez, no Python.
- Linhas
- Colunas
- Dados heterogêneos (diferentes tipos em diferentes colunas)
![DataFrame no Python](/imgs/dataframe.svg)

### Series
As Series nada mais são que as colunas em nossos DataFrames, caso fizessemos um recorte dos dados somente de uma coluna, isso seria uma "Series"
![Series no Python](/imgs/Series.svg)

### Filtragem de dados
Na filtragem de dados com pandas, quando usamos a sintaxe `notas['Coluna'] > 80` criamos uma máscara boolena - um array com valores True e False para cada linha onde True indica que a condição foi satisfeita. Depois, essa máscara é usada dentro dos colchetes `notas[]` para selecionar apenas as linhas onde o valor é True.

![Filtragem no pandas](/imgs/Filtragem.svg)