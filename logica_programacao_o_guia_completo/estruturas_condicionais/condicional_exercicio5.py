print('Digite um número: ')
valor = int(input())

if 1 <= valor <= 9:
    print('O valor está dentro da faixa permitida')
elif valor < 1 or valor > 11:
    print('O valor está fora da faixa permitida')