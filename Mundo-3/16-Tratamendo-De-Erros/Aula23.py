try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que foram informados.')
except ZeroDivisionError:
    print('Não é possivel dividir por zero.')
except KeyboardInterrupt:
    print('O usuário prefiriu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O Resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
