import pandas as pd

# dados = {
#   'Nome': ['Ana','Bruno','Carlos','Diana'],
#   'Idade': [25,30,22,28],
#   'Cidade':['São Paulo','Rio De Janeiro','Belo horizonte','Porto Alegre']
# }

# df = pd.DataFrame(dados)

# # Visualizar o DataFrame
# print(df)

# #Acessar uma coluna
# print('Coluna de idades:')
# print(df['Idade'])
# print(df['Nome'])

# # Informações básicas
# print('Informações do DataFrame:')
# print(df.info())

# # Estatísticas descritivas:
# print('Estatísticas descritivas:')
# print(df.describe())

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