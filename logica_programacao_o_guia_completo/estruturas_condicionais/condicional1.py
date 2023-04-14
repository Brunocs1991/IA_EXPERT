print('Digite a noda M1: ')
m1 = float(input())
print('Digite a noda M2: ')
m2 = float(input())
print('Digite a noda M3: ')
m3 = float(input())

media = (m1 + m2 + m3) / 3
print('Média: ', media)

if media > 6:
    print('Aluno aprovado!')
elif media < 4:
    print('Aluno reprovado')
elif 4 <= media < 6:
    print('Aluno pegou exame!')
    print('Digite a nota do exame: ')
    exame = float(input())
    if exame >= 6:
        print('Aluno aprovado no exame')
    else:
        print('Aluno reprovado no exame!')