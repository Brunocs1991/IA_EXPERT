print('Digite o primeiro valor: ')
valor1 = float(input())
print('Digite o segundo valor: ')
valor2 = float(input())
print('Digite a operação: ')
operacao = input()

if operacao == '+':
    resultado = valor1 + valor2
    print('Resultado: ', resultado)
elif operacao == '-':
    resultado = valor1 - valor2
    print('Resultado: ', resultado)
elif operacao == '*':
    resultado = valor1 * valor2
    print('Resultado: ', resultado)
elif operacao == '/':
    resultado = valor1 / valor2
    print('Resultado: ', resultado)
else:
    print('Operação inválida')
