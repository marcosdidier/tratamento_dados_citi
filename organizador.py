import pandas as pd

baseDesorganizada = pd.read_csv('baseDesorganizada.csv')

mapeamento = {
    'fem': 'Feminino',
    'F': 'Feminino',
    'masc': 'Masculino',
    'M': 'Masculino'
}

def tratarMedia(x):
    return str(x).replace('.', ',')


def tratarNotas(x):
    return float(str(x).replace(',', '.'))


baseDesorganizada['sexo'] = baseDesorganizada['sexo'].map(lambda x: mapeamento.get(x, x))

baseDesorganizada['nota_matematica'] = baseDesorganizada['nota_matematica'].map(tratarNotas)
baseDesorganizada['nota_portugues'] = baseDesorganizada['nota_portugues'].map(tratarNotas)


baseDesorganizada['media'] = (baseDesorganizada['nota_matematica'] + baseDesorganizada['nota_portugues'] + (baseDesorganizada['frequencia'] / 10) ) / 3

baseDesorganizada['nota_matematica'] = baseDesorganizada['nota_matematica'].map(tratarMedia)
baseDesorganizada['nota_portugues'] = baseDesorganizada['nota_portugues'].map(tratarMedia)

baseDesorganizada['aprovado'] = baseDesorganizada['media'].map(lambda x: 'Sim' if x >= 7 else 'Não')

baseDesorganizada.to_csv('baseTratada.csv', index=False)