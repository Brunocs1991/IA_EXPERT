print('Digite o primeiro valor: ')
valor1 = float(input())
print('Digite o segundo valor: ')
valor2 = float(input())
print('Digite a operação: ')
operacao = input()

match operacao:
    case '+':
        resultado = valor1 + valor2
        print('Resultado: ', resultado)
    case '-':
        resultado = valor1 - valor2
        print('Resultado: ', resultado)
    case '*':
        resultado = valor1 * valor2
        print('Resultado: ', resultado)
    case '/':
        resultado = valor1 / valor2
        print('Resultado: ', resultado)
    case _:
        print('Operação invalida!')
