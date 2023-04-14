"""
(Usuario) ler os valores de comprimento, largura e altura e apresentar o valor do volume
de uma caixa retangular. Utilize para o cálculo e fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA.
Ao final do calculo perguntar ao usuário se deseja continuar o programa fazendo nova leitura
"""

continua = 's'
while continua == 's':
    print('Digite a comprimento: ')
    comprimento = float(input())
    print('Digite a largura: ')
    largura = float(input())
    print('Digite a altura: ')
    altuta = float(input())

    volume = comprimento * altuta * largura
    print('Volume: ', volume)
    print('Deseja ler mais valores (s/n)?')
    continua = input()
