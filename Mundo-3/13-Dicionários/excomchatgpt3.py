estoque = []
while True:
    produto = {
        'Nome': input('Nome do produto: '),
        'Preço': float(input('Preço: R$ ')),
        'Quantidade': int(input('Quantide em estoque: '))
    }
    estoque.append(produto)
    go = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while go not in 'SN':
        print('ERRO! Por favor digite apenas S ou N')
        go = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if 'N' in go:
        break
print('\n<<< PRODUTOS CADASTRADOS >>>\n')
for v in estoque:
    total = v['Preço'] * v['Quantidade']
    print(f'Produto: {v["Nome"]} | Preço: R${v["Preço"]:.2f} | Quantidade: {v["Quantidade"]} | Total: R$ {total:.2f}')
nome_alterar = input('Nome do produto que deseja atualizar o preço: ')
encontrado = False
for v in estoque:
    if nome_alterar.lower() == v['Nome'].lower():
        print('\nProduto encontrado!')
        novo_preço = float(input(f'Digite o novo preço para {v["Nome"]}: R$ '))
        v['Preço'] = novo_preço
        print(f'Preço atualizado com sucesso! O preço de {v["Nome"]} agora é R$: {v["Preço"]}')
        encontrado = True
        break
if not encontrado:
    print('\nProduto não encontrado.')
total_geral = 0
for v in estoque:
    total_geral += v['Preço'] * v['Quantidade']
print(f'Valor total geral em estoque: R${total_geral:.2f}')