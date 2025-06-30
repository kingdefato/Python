pessoa = {
    'Nome': input('Nome: '),
    'Idade': int(input('Idade: ')),
    'Cidade': input('Cidade: ')
}
print(f'{pessoa["Nome"]} tem {pessoa["Idade"]} anos e mora em {pessoa["Cidade"]}')