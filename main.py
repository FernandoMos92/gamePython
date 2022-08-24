import guessing
import gibbet

def choice_game():
    print("*********************************")
    print("********ESCOLHA SEU JOGO*********")
    print("*********************************")

    print("(1) Gibbet (2) Guessing")
    game = int(input("Qual jogos?"))

    if game == 1:
        print("Jogando Gibbet")
        gibbet.play_gibbet()
    elif game == 2:
        print("Jogando Guessing")
        guessing.play_guessing()
if(__name__ == "__main__"):
  choice_game()