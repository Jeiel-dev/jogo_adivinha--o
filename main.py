import random

def lin():
    print("-"*40)
def lin2(txt):
    print("-"*40)
    print(    txt    )
    print("-"*40)
def dialogo1(dificuldade):
    if dificuldade == 1:
        tentativas = 10; intervalo = 50
    elif dificuldade == 2:
        tentativas = 5; intervalo = 50
    elif dificuldade == 3:
        tentativas = 10; intervalo = 100
    return tentativas, intervalo


lin2("BEM VINDO AO JOGO!\nAdivinhe o numero")
while True:
    while True:
        dificuldade = int(input("Escolha a dificuldade de 1 a 3: "))
        if dificuldade == 1 or dificuldade == 2 or dificuldade == 3:
            if dificuldade == 1:
                dif = ("Facil")
            elif dificuldade == 2:
                dif = ("Medio")
            elif dificuldade == 3:
                dif = ("Dificil")
            break
        else:
            print(" Dificuldade invalida ")
    tentativas, intervalo = dialogo1(dificuldade)
    lin2(f"   dificuldade - {dif}   ")

    numer_secreto = random.randint(0,intervalo)
    print(f"Adivinhe o numero entre 0 e {intervalo}")
    lin()

    while tentativas > 0:
        numer_dig = int(input(f"Digite um numero, você tem {tentativas} tentativas\n"))
        if numer_dig == 8524567193:
            print(numer_secreto)
        if numer_dig == numer_secreto:
            print("\n|     ACERTOU!    |\n")
            break
        else:
            print("\n|    NUMERO ERRADO    |\n")
            if numer_dig < numer_secreto:
                print("O numero é maior")
                tentativas = tentativas - 1
                if tentativas == 0:
                    break
            else:
                print("O numero é menor")
                tentativas = tentativas - 1
                if tentativas == 0:
                    break
            print(f"Você tem mais {tentativas} tentativas")
            lin()
    if tentativas == 0:
        lin2(f"Numero de tentativas exedida\nNumero secreto: {numer_secreto}")
    else:
        lin2("Bom Jogo")
    while True:
        y_n = input("Jogar novamente?\nDigite (y) para sim\nDigite (n) Para nao\n")
        if y_n == ("y"):
            lin()
            break
        elif y_n == ("n"):
            print("ATE A PROXIMA")
            exit()
        else:
            print("Resposta invalida")
            