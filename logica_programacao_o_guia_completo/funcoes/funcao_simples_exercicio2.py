C = 0
F = 0


def leitura():
    print("Digite a temperatura em graus Celsius: ")
    global C
    C = float(input())


def conversao():
    global F
    F = (9 * C + 160) / 5


def resultado():
    print("Temperatura em F: ", F)


if __name__ == "__main__":
    leitura()
    conversao()
    resultado()
