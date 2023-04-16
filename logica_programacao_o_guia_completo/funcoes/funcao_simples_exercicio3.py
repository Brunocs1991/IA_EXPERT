tempo = 0
velocidade = 0
distancia = 0
litros = 0


def leitura():
    print("Digite o tempo da viagem: ")
    global tempo
    tempo = int(input())
    print("Digite a velocidade média: ")
    global velocidade
    velocidade = float(input())


def calcula_distancia():
    global distancia
    distancia = tempo * velocidade


def calcula_litros():
    global litros
    litros = distancia / 12


def resultado():
    print("Tempo: ", tempo)
    print("Velocidade: ", velocidade)
    print("Distancia: ", distancia)
    print("Litros: ", litros)


if __name__ == "__main__":
    leitura()
    calcula_distancia()
    calcula_litros()
    resultado()
