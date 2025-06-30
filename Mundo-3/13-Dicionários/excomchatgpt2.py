produto = {
    'Nome': input('Nome do produto: '),
    'Preço': float(input('Preço: R$ ')),
    'Quantidade': int(input('Quantidade em estoque: '))
}
total = produto['Preço'] * produto['Quantidade']
print(f'O produto {produto["Nome"]} custa R${produto["Preço"]} e há {produto["Quantidade"]} em estoque.\nValor total em estoque: R${total:.2f}')