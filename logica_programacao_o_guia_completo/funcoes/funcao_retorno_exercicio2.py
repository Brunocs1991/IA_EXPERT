def leitura():
    print("Digite um número: ")
    return int(input())


def positivo(numero):
    if numero >= 0:
        return True
    else:
        return False


if __name__ == '__main__':
    numero = leitura()
    resultado = positivo(numero)
    if resultado:
        print(numero, 'é Positivo!')
    else:
        print(numero, 'é Negativo!')
