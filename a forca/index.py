import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "algoritmo", "inteligencia"]
    return random.choice(palavras)

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    mostrar_forca(palavra_secreta, letras_corretas)

    while tentativas > 0:
        letra = input("Digite uma letra: ")

        if letra in letras_corretas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            letras_corretas.append(letra)
        else:
            print("Letra errada!")
            tentativas -= 1

        mostrar_forca(palavra_secreta, letras_corretas)

        if all(letra in letras_corretas for letra in palavra_secreta):
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    jogar_forca()