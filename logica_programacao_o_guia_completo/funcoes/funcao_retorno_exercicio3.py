def leitura(mensagem):
    print(mensagem)
    return float(input())


def calcula_distancia(tempo, velocidade):
    return tempo * velocidade


def calcula_litros(distancia):
    return distancia / 12


def resultado(t, v, d, l):
    print("Tempo: ", t)
    print("Velocidade: ", v)
    print("Distância: ", d)
    print("Litros: ", l)


if __name__ == '__main__':
    tempo = leitura("Digite o tempo gasto na viagem: ")
    velocidade = leitura("Digite a velocidade média: ")
    distancia = calcula_distancia(tempo, velocidade)
    litros = calcula_litros(distancia)
    resultado(tempo, velocidade, distancia, litros)
