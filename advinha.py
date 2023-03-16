print ("*********************************")
print ("        jogo do arch")
print ("*********************************")

numero_secreto = 42
max_tentativa = 3
tentativa = 1

while(tentativa <= max_tentativa):
    print("Tentativa {} de {} tentativas".format(tentativa, max_tentativa))
    chute_str = input ("digite seu numero ")
    chute = int(chute_str)
    print("voce digitou", chute)

    acertou = numero_secreto == chute
    erroupracima = chute > numero_secreto
    errouprabaixo = chute < numero_secreto

    if (acertou):
        print ("acerto mizeravi")
    else:
        if(erroupracima):
            print ("errou pra cima fiote")
        elif(errouprabaixo):
            print ("errou pra baixo fi")
    tentativa = tentativa + 1

print("sai fora")