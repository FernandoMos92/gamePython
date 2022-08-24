
def play_gibbet():
    print('************************')
    print('***Bem-vindo ao jogo Gibbet!***')
    print('************************')

    secret_word = "banana"

    hanged = False
    hit = False

    while not hit and not hanged:
      
        user_kick = input("Qual letra? ").strip()
        position_letter = 0
        for letter in secret_word:
            if letter.upper() == user_kick.upper():
                print("Encontrei a letra {} na posição {}.".format(letter, position_letter))
            position_letter = position_letter + 1

        print("Jogando...")

    print("Fim do jogo")


if (__name__ == "__main__"):
    play_gibbet()