# Jogo de adivinhação

# No jogo, o usuário precisa adivinhar um número secreto
#Ele pode tentar várias vezes até acertar 

numero_secreto = 5
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar um número de 01 a 10: "))

    if tentativa > numero_secreto:
        print("O número secreto é menor!")
    elif tentativa < numero_secreto:
        print("O número secreto é maior!")
    else:
        print("Parabéns, você acertou!")




