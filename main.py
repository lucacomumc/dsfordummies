import pandas as pd

dados = {
  'Nome': ['Ana','Bruno','Carlos','Diana'],
  'Idade': [25,30,22,28],
  'Cidade':['São Paulo','Rio De Janeiro','Belo horizonte','Porto Alegre']
}

df = pd.DataFrame(dados)

# Visualizar o DataFrame
print(df)

#Acessar uma coluna
print('Coluna de idades:')
print(df['Idade'])
print(df['Nome'])

# Informações básicas
print('Informações do DataFrame:')
print(df.info())

# Estatísticas descritivas:
print('Estatísticas descritivas:')
print(df.describe())

dados2 = {
  'Aluno': ['Ana','Bruno','Carlos','Diana','Eduardo'],
  'Matemática':[85,78,92,88,76],
  'Português':[90,82,78,95,86],
  'Ciências':[88,81,85,92,79]
}

notas = pd.DataFrame(dados2)

print(notas)

# Acessando uma coluna específica:
print('Notas de matemática:')
print(notas['Matemática'])

# Selecionando um subconjunto de dados:
print('Alunos com nota de Matemática acima de 80')
print(notas[notas['Matemática'] > 80])

# Adicionando uma nova coluna (média das notas)
notas['Média'] = (notas['Matemática'] + notas['Português'] + notas['Ciências']) / 3
print('DataFrame com a coluna de média:')
print(notas)

# Ordenação de dados

# Ordenando por uma coluna (ordem crescente):
notas_ordenadas = notas.sort_values(by='Matemática')
print('Ordenado por notas de Matemática (crescente):')
print(notas_ordenadas)

# Ordenando por uma coluna (ordem decrescente):
notas_decrescente = notas.sort_values(by='Matemática', ascending=False)
print('\nOrdenado por notas de Matemática (decrescente):')
print(notas_decrescente)

# Ordenando por múltiplas colunas:
notas_mult = notas.sort_values(by=['Português','Matemática'], ascending=[False,True])
print('\nOrdenado por Português (decrescente) e Matemática (crescente):')
print(notas_mult)

# Agrupamento de dados

alunos_dict = {
  'Nome':['Ana','Bruno','Carlos','Diana','Eduardo'],
  'Turma':['A','B','A','B','A'],
  'Nota':[85,78,92,88,76]
}

alunos = pd.DataFrame(alunos_dict)
print('\nDataFrame de Alunos:')
print(alunos)

# Agrupando por Turma e calculando a média
media_por_turma = alunos.groupby('Turma')['Nota'].mean()
print('\nMédia de notas por turma:')
print(media_por_turma)

# Agrupando e aplicando múltiplas funções
estatisticas_turma = alunos.groupby('Turma')['Nota'].agg(['mean', 'min', 'max'])
print('\nEstatísticas de notas por turma:')
print(estatisticas_turma)

# Agrupamento com múltiplas colunas
alunos['Sexo'] = ['Feminino', 'Masculino', 'Masculino', 'Feminino', 'Masculino']
multi_grupo = alunos.groupby(['Turma', 'Sexo'])['Nota'].mean()
print('\nMédia de notas por turma e sexo:')
print(multi_grupo)

# Tratamento de dados ausentes

dados_faltantes = pd.DataFrame({
    'A':[1,2,None,4,5],
    'B':[None,2,3,None,5],
    'C':[1,2,3,4,5]
})

print('DataFrame com dados faltantes:')
print(dados_faltantes)

# Verificando dados ausentes:
print(dados_faltantes.isna()) # Retorna True onde há valores ausentes

# Contando valores ausentes por coluna:
print(dados_faltantes.isna().sum())

# Preenchendo valores ausentes com 0:
preenchido_valor = dados_faltantes.fillna(0)
print('Preenchido com 0:')
print(preenchido_valor)

# Preenchendo com o valor anterior ou posterior
preenchido_anterior = dados_faltantes.fillna(method='ffill')  # forward fill
print("\nSubstituindo ausentes pelo valor anterior:")
print(preenchido_anterior)

# Removendo linhas com valores ausentes
sem_ausentes = dados_faltantes.dropna()
print("\nRemovendo linhas com valores ausentes:")
print(sem_ausentes)


# Criando dois DataFrames para combinar
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Departamento': ['RH', 'Vendas', 'TI', 'Marketing']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Salário': [5000, 6000, 7500, 8000],
    'Bônus': [500, 1000, 0, 2000]
})

print("DataFrame 1 (Funcionários):")
print(df1)
print("\nDataFrame 2 (Salários):")
print(df2)

# Merge (similar ao JOIN em SQL)
# Inner join - apenas registros que existem em ambos os DataFrames
merge_inner = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Join (apenas IDs que existem em ambos):")
print(merge_inner)

# Left join - todos os registros do DataFrame da esquerda
merge_left = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join (todos os funcionários, mesmo sem salário):")
print(merge_left)

#  Outer join - todos os registros de ambos os DataFrames
merge_outer = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join (todos os registros de ambos):")
print(merge_outer)