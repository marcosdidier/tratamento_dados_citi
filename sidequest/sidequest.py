import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def tratarNotas(x):
    return float(str(x).replace(',', '.'))

base = pd.read_csv('baseTratada.csv')
baseSidequest = base.copy()

aprovados = baseSidequest['aprovado'].value_counts()
percentualAprovados = baseSidequest['aprovado'].value_counts(normalize=True) * 100

print('Quantidade de alunos aprovados: ')
print(aprovados.to_dict())
print('Percentual de alunos aprovados: ')
print(percentualAprovados.to_dict())

plt.pie(aprovados.values, labels=aprovados.index, autopct='%1.1f%%')
plt.title('Porcentagem de aprovados')
plt.show()

sexo = baseSidequest['sexo'].value_counts()
print('\nDistribuição por sexo: ')
print(sexo.to_dict())

sns.barplot(x=sexo.index, y=sexo.values)
plt.title('Distribuição por sexo')
plt.xlabel('Sexo')
plt.ylabel('Quantidade por sexo')
plt.show()

baseMelhoresMedias = base.copy()
baseMelhoresMedias['media'] = baseMelhoresMedias['media'].map(tratarNotas)
baseMelhoresMedias = baseMelhoresMedias.sort_values('media', ascending=False)

top5 = baseMelhoresMedias[['nome', 'media']].head(5)
print(f'\n Top 5 médias: \n{top5}')

top5['media']= top5['media'].map(tratarNotas)
sns.barplot(x='nome', y='media', data=top5)
plt.title('Melhores médias')
plt.xlabel('Nome do aluno')
plt.ylabel('Média do aluno')
plt.show()

baseMelhoresFrequencias = base.copy()
baseMelhoresFrequencias = baseMelhoresFrequencias.sort_values('frequencia', ascending=False)

top5Frequencias = baseMelhoresFrequencias[['nome', 'frequencia']].head(5)
print(f'\n Top 5 alunos mais assíduos: \n{top5Frequencias}')

sns.barplot(x='nome', y='frequencia', data=top5Frequencias)
plt.title('Gráfico de frequência dos 5 alunos mais assíduos')
plt.xlabel('Nome do aluno')
plt.ylabel('Frequência')
plt.show()