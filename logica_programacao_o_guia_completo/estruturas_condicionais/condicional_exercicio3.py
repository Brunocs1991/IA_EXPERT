print('Digite a idade do usuário: ')
idade = int(input())

if 0 <= idade <= 12:
    print('Criança')
elif 13 <= idade <= 17:
    print('Adolescente')
elif idade >= 18:
    print('Adulto')
else:
    print('Idade inválida')
