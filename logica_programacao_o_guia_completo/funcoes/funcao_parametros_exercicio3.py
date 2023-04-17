idade = 0


def leitura(msg):
    print(msg)
    global idade
    idade = int(input())


def faixa(id):
    if 0 <= id <= 12:
        print("Criança")
    elif 13 <= id <= 17:
        print("Adolescente")
    elif id >= 18:
        print("Adulto")
    else:
        print("Idade inválida")


if __name__ == "__main__":
    leitura("Digite a idade do usuário: ")
    faixa(idade)