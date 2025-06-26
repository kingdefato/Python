'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
 Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.'''
dados = {'Titulo':'Como treinar o seu Dragão','Ano':'2014','Genero':'Ficção Cientifica'}
dados['Diretor'] = 'Ytallo'
for k, v in dados.items():
    print(f'O {k} é {v}')  
#print(f'O titulo é {dados["Titulo"]} e o genero é {dados["Genero"]}')

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range (0, 3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #não funciona para dicionarios [:], usar metodo interno .copy()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()