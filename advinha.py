import random
def jogar():
    print ("*********************************")
    print ("        jogo do arch")
    print ("*********************************")

    numero_secreto = random.randrange(1, 100+1)
    print (numero_secreto)
    pontos = 1000

    print ("escolha um nivel")
    print ("facil (1)=6 tentativas")
    print ("medio (2)=5 tentativas")
    print ("dificil (3)=3 tentativas")


    nivel = int(input("digite o nivel "))

    if nivel == 1:
        total_de_tentativas = 6
    elif nivel == 2:
        total_de_tentativas = 5
    elif nivel == 3:
        total_de_tentativas = 3



    #while(tentativa <= max_tentativa):
    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {} tentativas".format(rodada, total_de_tentativas))
        chute_str = input ("digite seu numero ")
        chute = int(chute_str)
        print("voce digitou", chute)
        acertou = numero_secreto == chute
        erroupracima = chute > numero_secreto
        errouprabaixo = chute < numero_secreto
        if (acertou):
            print ("acerto mizeravi, voce fez {} pontos".format(pontos))
            break
        else:
            if(erroupracima):
                print ("errou pra cima fiote")
            elif(errouprabaixo):
                print ("errou pra baixo fi")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("sai fora")
if (__name__ == "__main__"):
    jogar()