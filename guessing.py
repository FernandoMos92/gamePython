import random


def play_guessing():

    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")
    secret_number = random.randrange(1, 101)
    max_attempt = 0
    points = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    level = int(input("Defina o nível: "))

    if (level == 1):
        max_attempt = 20
    elif (level == 2):
        max_attempt = 10
    else:
        max_attempt = 5

    for round_player in range(1, max_attempt + 1):
        print("Tentativa {} de {}".format(round_player, max_attempt))

        user__attempt = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", user__attempt)
        user__attempt = int(user__attempt)

        if (user__attempt < 1 or user__attempt > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        win = user__attempt == secret_number
        bigger_then = user__attempt > secret_number
        less_then = user__attempt < secret_number

        if (win):
            print("Você acertou e fez {} pontos!".format(points))
            break
        else:
            if (bigger_then):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (less_then):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            points_lost = abs(secret_number - user__attempt)
            points = points - points_lost


if(__name__ == "__main__"):
  play_guessing()


print("Fim do jogo")