import advinha
import forca

def menu_jogos():
    print ("**************************")
    print ("********jogos arch********")
    print ("**************************")
    print ("      Qual seu jogo?")
    print ("Escolha 1 para jogar forca")
    print ("Escolha 2 para jogar adivinhacao")
    game = int (input ())

    if game == 1:
        forca.jogar()
    elif game == 2:
        advinha.jogar()
if (__name__ == "__main__"):
    menu_jogos()