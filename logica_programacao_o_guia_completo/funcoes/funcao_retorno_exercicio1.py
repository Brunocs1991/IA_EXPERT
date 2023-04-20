def leitura(mensagem):
    print(mensagem)
    valor = int(input())
    return valor


def calcula_media(v1, v2, v3):
    return (v1 + v2 + v3) / 3


def resultado(media):
    print("Média: ", media)


if __name__ == "__main__":
    valor1 = leitura("Digite o primeiro valor: ")
    valor2 = leitura("Digite o segundo valor: ")
    valor3 = leitura("Digite o terceiro valor: ")
    media = calcula_media(valor1, valor2, valor3)
    resultado(media)
