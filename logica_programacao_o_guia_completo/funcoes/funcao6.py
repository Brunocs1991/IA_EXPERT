def leitura():
    print("Digite o valor: ")
    valor = int(input())
    return valor


def valida_numero(nr):
    if nr < 0:
        return False
    else:
        return True


if __name__ == '__main__':
    numero = leitura()
    resultado = valida_numero(numero)
    print(resultado)
